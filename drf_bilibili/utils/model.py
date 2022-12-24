from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """基类模型"""
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True  # 抽象模型类, 用于继承使用