import datetime

SIMPLE_JWT = {
    # token有效时长(返回的 access 有效时长)
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    # token刷新的有效时间(返回的 refresh 有效时长)
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema', # 接口文档配置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    #
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # 全局频率
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'rest_framework.throttling.AnonRateThrottle',
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/m',
    # },

    # 'PAGE_SIZE': 2,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    # 全局配置异常模块
    'EXCEPTION_HANDLER': 'utils.exception.custom_exception_handler',

    # 修改默认返回JSON的renderer的类
    'DEFAULT_RENDERER_CLASSES': (
        # 'rest_framework.renderers.JSONRenderer', # 默认的jsonrender类
        'rest_framework.renderers.BrowsableAPIRenderer',
        'utils.rendererresponse.customrenderer',
    ),
}

# drf-extentions
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

