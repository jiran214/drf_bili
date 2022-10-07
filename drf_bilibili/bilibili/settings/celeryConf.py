
"""
Celery 配置
"""

# 最重要的配置，设置消息broker,格式为：db://user:password@host:port/dbname
# 如果redis安装在本机，使用localhost
# 如果docker部署的redis，使用redis://redis:6379
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

# celery时区设置，建议与Django settings中TIME_ZONE同样时区，防止时差
# Django设置时区需同时设置USE_TZ=True和TIME_ZONE = 'Asia/Shanghai'
CELERY_TIMEZONE = 'Asia/Shanghai'

# 为django_celery_results存储Celery任务执行结果设置后台
# 格式为：db+scheme://user:password@host:port/dbname
# 支持数据库django-db和缓存django-cache存储任务状态及结果
CELERY_RESULT_BACKEND = "django-db"
# celery内容等消息的格式设置，默认json
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# 为任务设置超时时间，单位秒。超时即中止，执行下个任务。
CELERY_TASK_TIME_LIMIT = 5

# 为存储结果设置过期日期，默认1天过期。如果beat开启，Celery每天会自动清除。
# 设为0，存储结果永不过期
# CELERY_RESULT_EXPIRES = xx

# 任务限流
CELERY_TASK_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

# Worker并发数量，一般默认CPU核数，可以不设置
CELERY_WORKER_CONCURRENCY = 2

# 每个worker执行了多少任务就会死掉，默认是无限的
CELERY_WORKER_MAX_TASKS_PER_CHILD = 200

# 定时
from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    "add-every-30s": {
        "task": "apps.note.tasks.add",
        'schedule': 60*60,  # 每30秒执行1次
        'args': (1, 11)  # 传递参数-
    },
    # "add-every-day": {
    #     "task": "note.tasks.add",
    #     'schedule': timedelta(hours=1), # 每小时执行1次
    #     'args': (1, 1) # 传递参数-
    # },
}
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

"""邮件配置"""
# 配置邮件发送
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'  # 如果为163邮箱，设置为smtp.163.com
EMAIL_PORT = 25  # 或者 465/587是设置了 SSL 加密方式
# 发送邮件的邮箱
EMAIL_HOST_USER = '593848579@qq.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'kqzfddtesohgbbjb'  # 第三方登陆使用的授权密码
EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
# 收件人看到的发件人, 必须是一直且有效的
EMAIL_FROM = '593848579@qq.com'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER