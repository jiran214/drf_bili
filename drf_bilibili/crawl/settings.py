# Scrapy settings for crawl project
# django混用配置
import datetime
import os
import sys
import redis

sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'bilibili.settings.dev'  # 项目名.settings
import django

django.setup()

BOT_NAME = 'crawl'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50'
# LOG_LEVEL = 'INFO'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 减少请求并发数量
CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4
# 设置请求间隔
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 2
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Content-Type': 'application/json; charset=utf-8',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'crawl.middlewares.MyprojectSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'crawl.middlewares.CrawlDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'crawl.pipelines.MysqlPipeline': 700,
    'crawl.pipelines.RedisPipeline': 800,
    # 'crawl.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL = {
    'HOST': '127.0.0.1',  # 数据库主机
    'PORT': 3306,  # 数据库端口
    'USER': 'root',  # 数据库用户名
    'PASSWORD': '123456',  # 数据库用户密码
    'DATABASE': 'bili'  # 数据库名字
}

# redis conf
DOMAIN_HOST = '127.0.0.1'
REDIS_HOST = DOMAIN_HOST
REDIS_PASS = '123457'
REDIS_PORT = 6379
# 默认6379#57891

redis_conn = redis.StrictRedis(host=DOMAIN_HOST, port=REDIS_PORT, decode_responses=True)

# to_day = datetime.datetime.now()
# LOG_ENABLED = True
# LOG_FILE = "E:/project/Django-learn/drf_bili/drf_bilibili/crawl/log/{}{}{}.log".format(to_day.year, to_day.month,
#                                                                                      to_day.day)
# LOG_LEVEL = "INFO"
# # 显示日志级别以上的日志信息（包括自己）
# LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
# LOG_FORMAT = "%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-%(message)s-%(lineno)d"

# """日志配置"""
# filepath = 'singlefilename'
# if not os.path.isdir(LOG_FILE):
#     # 创建文件夹
#     os.mkdir(LOG_FILE)
