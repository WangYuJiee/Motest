# -*- coding: UTF-8 -*-
import copy
import pickle
import time

from redis import ConnectionError, Redis, StrictRedis


# redis的默认参数(host， port, db)其中db为定义redis database的数量
from db_data.config import redis_conf

redis_kwargs = {
    "host": redis_conf.HOST,
    "port": redis_conf.PORT,
    "db": redis_conf.CACHE_DB,
    "password": redis_conf.PASSWORD
}


class RedisCacheData(object):
    """
    redis缓存数据基类
    """
    redis_conn = None
    redis_pool = None
    user_cache_prefix = "user:user_info:"

    def __init__(self):
        rs = Redis(host=redis_conf.HOST,
                   port=redis_conf.PORT,
                   db=redis_conf.CACHE_DB,
                   password=redis_conf.PASSWORD)
        try:
            rs.ping()
            self.redis_conn = StrictRedis(**redis_kwargs)
            # self.redis_pool = self.redis_conn.connection_pool
        except ConnectionError:
            # in case of a lost connection lets sit and wait till it's online
            while not self.redis_conn:
                print('Attempting Connect To Redis...')
                self.__init__()

    def connections(self):
        self.redis_pool = self.redis_conn.connection_pool
        return self.redis_pool._created_connections

    # def inuse(self):
    #     return self.redis_pool._in_use_connections

    def exists_redis(self, key):
        return self.redis_conn.exists(key)

    def get_redis_info(self, key):
        """
        获取redis中缓存的信息，这里的查询，传入的参数必须加前缀
        :param key: 类似'point:' + {point_id}这种查询字段
        :return:
        """
        if not self.redis_conn:
            return None
        value = self.redis_conn.get(key)
        try:
            return pickle.loads(value) if value else None
        except Exception as e:
            return value

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """
        redis 更新或者创建key:value键值对，并且对值做了pickle.dumps持久化处理
        :param name: key name
        :param value: value
        :param ex: sets an expire flag on key ``name`` for ``ex`` seconds.
        :param px: sets an expire flag on key ``name`` for ``px`` milliseconds.
        :param nx: if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.
        :param xx: if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.
        :return:
        """
        if self.redis_conn and name and value:
            value = pickle.dumps(value)
            self.redis_conn.set(name, value, ex, px, nx, xx)

    def create_user_info_cache(self, email, message):
        """
        将用户信息缓存到redis中
        :param email: 查询的主要登录名称
        :param message: 存储的token等登录返回信息
        :return:
        """
        new_message = pickle.dumps(message)
        self.redis_conn.setex(name=self.user_cache_prefix + email,
                              time=redis_conf.USER_STATUS_MAINTAIN_TIME,
                              value=new_message)

    def get_user_info_cache(self, key):
        """
        将用户信息缓存到redis中
        :key: 用户名
        :return:
        """
        keyd = self.user_cache_prefix+key
        if not self.redis_conn:
            return None
        value = self.redis_conn.get(keyd)
        try:
            return pickle.loads(value) if value else None
        except Exception as e:
            return value

    def update_user_info_cache_time(self, email):
        """
        更新用户信息缓存时间
        :param email:
        :return:
        """
        cache_time = redis_conf.USER_STATUS_MAINTAIN_TIME
        self.redis_conn.expire(self.user_cache_prefix + email, cache_time)

    def delete_user_cache(self, email):
        # 删除用户缓存在redis中的信息
        self.redis_conn.delete(self.user_cache_prefix + email)

    def delete(self, key):
        # 删除key缓存在redis中的信息
        self.redis_conn.delete(key)

    def clear_cache_ns(self, pattern):
        """
        Clears a namespace in redis cache.
        :param pattern: str, namespace i.e your:prefix*
        :return: int, num cleared keys
        """
        if not self.redis_conn:
            return None
        # for key in self.redis_conn.keys(pattern + '*'):
        for key in self.redis_conn.keys(pattern):
            self.redis_conn.delete(key)
        return True


    def mget_redis_cache(self, key):
        if self.redis_conn and key:
            if isinstance(key, list):
                return [pickle.loads(res) for res in self.redis_conn.mget(key)
                        if res]
            else:
                result = self.get_redis_info(key)
                return list(result) if result else []
        else:
            return []

    def mset_redis_cache(self, key_dict, ttl_time=-1):
        """
        批量存储数据, 详见：http://redisdoc.com/string/mset_redis_cache.html
        :param key_dict:
        :param ttl_time: 过期时间
        :return:
        """
        if isinstance(key_dict, list):
            # 实时数据的列表, 转换为key-value形式
            key_dict = {'point:' + str(i["pointid"]): pickle.dumps(i)
                        for i in key_dict if i["pointid"]}

        if self.redis_conn and key_dict:
            self.redis_conn.mset(key_dict)
            # 批量设置过期时间
            if ttl_time != -1:
                pipe = self.redis_conn.pipeline(transaction=False)
                for key in key_dict:
                    pipe.expire(key, ttl_time)
                pipe.execute()

    def create_redis_info_cache(self, key, value, ttl_time=300):
        """
        创建缓存
        :param key:
        :param value:
        :param ttl_time: 设置缓存过期时间
        :return:
        """
        if not self.redis_conn:
            return None
        # 将区域导航信息加入redis
        new_message = pickle.dumps(value)
        self.redis_conn.setex(name=key, time=ttl_time, value=new_message)

    # redis中的hash存储
    def update_redis_hash_info(self, key, hkey, value):
        new_message = pickle.dumps(value)
        self.redis_conn.hset(key, hkey, new_message)

    def get_redis_hash(self, key, hkey):
        message = self.redis_conn.hget(key, hkey)
        new_message = pickle.loads(message)
        return new_message

    def exists_redis_hash(self, key, hkey):
        res = self.redis_conn.hexists(key, hkey)
        if res:
            return res
        else:
            return None

    def redis_incr(self, key, ex_time):
        """
        查询key的调用次数以及key的过期时间
        :param key:
        :param ex_time:
        :return:
        """
        # 如果没有查到key,则默认返回1，否则，自增
        res = self.redis_conn.incr(key)
        # 如果是第一次查询，则设置过期时间
        if res == 1:
            self.redis_conn.expire(key, ex_time)
        return res


redis_cache = RedisCacheData()




