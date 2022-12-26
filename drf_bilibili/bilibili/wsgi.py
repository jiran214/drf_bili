"""
WSGI config for bilibili project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# 环境选择全在这配置
# profile = os.environ.get("PROJECT_PROFILE", 'dev')
profile = os.environ.get("PROJECT_PROFILE", 'prod')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilibili.settings.{}'.format(profile))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilibili.settings.prod')

application = get_wsgi_application()
