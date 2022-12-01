from .base import *
from .log import *
from .celeryConf import *
from .drfConf import *

DEBUG = True
# 其他相关配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        # 'HOST': 'db',
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '',  # 数据库用户密码
        'NAME': 'bili',  # 数据库名字
        'OPTIONS' : { 'charset' : 'utf8mb4' },
    }
}

CACHES = {

    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',  # redis所在服务器或容器ip地址
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",  # 你设置的密码
        },
    },
}