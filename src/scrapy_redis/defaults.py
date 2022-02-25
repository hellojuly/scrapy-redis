import redis


# For standalone use.
DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

PIPELINE_KEY = '%(spider)s:items'

STATS_KEY = '%(spider)s:stats'

REDIS_CLS = redis.StrictRedis
REDIS_ENCODING = 'utf-8'
# Sane connection defaults.
REDIS_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'encoding': REDIS_ENCODING,
}

SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER_PERSIST = False
START_URLS_KEY = '%(name)s:start_urls'
START_URLS_AS_SET = False
START_URLS_AS_ZSET = False
MAX_IDLE_TIME = 0

# 默认指纹过期时间1天，24*60*60=86400
SCHEDULER_DUPEFILTER_EXPIRE_TIME = 86400
# 指纹清理间隔1天
EXPIRE_FIGGERPRINTS_CLEAN_INTERVAL = 24 * 60 * 60
