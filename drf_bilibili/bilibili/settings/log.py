
# 日志配置
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOGS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'standard': {
            'format': '[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d]==>[%(message)s]'
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s]==>[%(message)s]'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_info.log'),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 向终端中输出日志
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'operation': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_operation.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'query': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_query.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'admin_error.log'),
            'maxBytes': 1024 * 1024 * 50,  # 50 MB
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },

    },
    'loggers': {
        # 记录视图中手动info日志
        'info': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 非GET方法操作日志
        'operation': {
            'handlers': ['operation', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # GET方法查询日志
        'query': {
            'handlers': ['query', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # 记录视图异常日志
        'error': {
            'handlers': ['error', 'console'],
            'level': 'ERROR',
            'propagate': True,
        }
    }
}
