from db_data.redis_cache import redis_cache

# 统一请求头
HEADERS = {"Connection": "keep-alive",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/91.0.4472.124 Safari/537.36"
           }

# 从redis获取用户的token信息
TOKEN = redis_cache.get_redis_info('user:admin')
