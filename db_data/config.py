import os
import configparser
import logging as logging_custom

# 设置log的格式, 默认的level为DEBUG
logging_custom.basicConfig(
    level=logging_custom.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)


class Configuration(object):

    def __init__(self, config_file='config.ini'):
        """
        获得配置文件内容
        :param config_file: str  文件名
        """
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   config_file)
        self.config = configparser.ConfigParser()
        self.config.read(config_path, encoding="utf-8")

    def get_config_by_tab_name_and_key(self, tab_name, k_name, k_type="str"):
        """
        根据模块名称和字段名获取配置
        :param tab_name: 块名称
        :param k_name:  配置名称
        :param k_type: 默认是字符串类型
        :return:
        """
        if k_type == "bool":
            return self.config.getboolean(tab_name, k_name)
        elif k_type == "int":
            return self.config.getint(tab_name, k_name)
        else:
            return self.config.get(tab_name, k_name)


class RedisConf(Configuration):
    def __init__(self, config_file='config.ini', config_name='REDIS_CACHE'):
        super(RedisConf, self).__init__(config_file=config_file)
        self.config_name = config_name
        self.__init_conf()

    def __init_conf(self):
        self.HOST = self.config.get(self.config_name, "HOST")
        self.PORT = self.config.get(self.config_name, "PORT")
        self.PASSWORD = self.config.get(self.config_name, "PASSWORD")
        self.CACHE_DB = self.config.get(self.config_name, "CACHE_DB")
        self.USER_STATUS_MAINTAIN_TIME = self.config.get(self.config_name,
                                                         "MAINTAIN_TIME")

        self.REDIS_CONN_STRING = 'redis://:{password}@{host}:{port}'.format(
            password=self.PASSWORD, host=self.HOST, port=self.PORT)


redis_conf = RedisConf(config_name='REDIS_CACHE')

