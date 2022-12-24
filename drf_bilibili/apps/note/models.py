# Create your models here.
from datetime import datetime

from django.db import models
from apps.kol.models import Info as KolInfo

from utils.model import BaseModel


# Create your models here.

class Info(BaseModel):
    #基本信息
    aid = models.CharField(unique=True,max_length=20,verbose_name="视频aid")
    bvid = models.CharField(unique=True,max_length=20,verbose_name="稿件ID")
    cid = models.CharField(unique=True,max_length=20,null=True,verbose_name="视频cid")
    copyright = models.IntegerField(null=True,choices=((1, "原创"), (2, "转载")))
    ctime = models.IntegerField(verbose_name="投稿时间")
    des = models.CharField(max_length=300,verbose_name="视频描述")
    duration =models.IntegerField(verbose_name="视频总时长")
    dynamic = models.CharField(max_length=500,verbose_name="视频同步发布的的动态的文字内容")
    tag = models.CharField(null=True,max_length=100,verbose_name="标签")

    #作者信息
    # mid=models.IntegerField(verbose_name="up主编号")
    mid = models.ForeignKey(null=True,to=KolInfo, to_field="mid", db_column='mid',related_name="notes", on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=50,verbose_name="up主名字")
    face=models.CharField(max_length=100,verbose_name="up主头像")

    pic=models.CharField(max_length=100,verbose_name="封面")
    pub_location=models.CharField(null=True,max_length=20,verbose_name="地址")
    pubdate=models.IntegerField(verbose_name="发布时间")
    short_link=models.CharField(null=True,max_length=100,verbose_name="视频链接")

    #分区信息
    tid=models.IntegerField(verbose_name="分区编号")
    title=models.CharField(max_length=100,verbose_name="视频标题")
    tname=models.CharField(max_length=10,verbose_name="二级分区")

    #状态数据
    view_n = models.IntegerField(default=0, verbose_name="播放数")
    danmaku = models.IntegerField(default=0, verbose_name="弹幕数")
    reply = models.IntegerField(default=0, verbose_name="评论数")
    favorite = models.IntegerField(default=0, verbose_name="收藏数")
    coin = models.IntegerField(default=0, verbose_name="投币数")
    share = models.IntegerField(default=0, verbose_name="分享数")
    like_n = models.IntegerField(default=0, verbose_name="点赞数")
    # update_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    # create_time=models.DateTimeField(null=True,default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '笔记'
        verbose_name_plural = verbose_name


    def __str__(self):
        return f'aid:{self.aid}-title:{self.title}'

class Stat(BaseModel):
    # 互动数据stat

    aid = models.ForeignKey(to=Info, to_field="aid",db_column='aid', related_name="states", on_delete=models.CASCADE)
    view_n = models.IntegerField(default=0, verbose_name="播放数")
    danmaku = models.IntegerField(default=0, verbose_name="弹幕数")
    reply = models.IntegerField(default=0, verbose_name="评论数")
    favorite = models.IntegerField(default=0, verbose_name="收藏数")
    coin = models.IntegerField(default=0, verbose_name="投币数")
    share = models.IntegerField(default=0, verbose_name="分享数")
    like_n = models.IntegerField(default=0, verbose_name="点赞数")
    # create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'aid:{self.aid}-hot_word:{self.view_n}'

class Danmu(BaseModel):
    cid = models.ForeignKey(to=Info, to_field="cid", db_column='cid',related_name="danmus", on_delete=models.CASCADE)
    content = models.CharField(max_length=100, verbose_name="弹幕内容")
    # ctime = models.CharField(max_length=10,verbose_name="发布时间")

    class Meta:
        verbose_name = '弹幕'
        verbose_name_plural = verbose_name

class Comment(BaseModel):

    aid=models.ForeignKey(to=Info,to_field="aid",db_column='aid',related_name="comments",on_delete=models.CASCADE)
    content = models.CharField(max_length=300, verbose_name="评论内容")
    like_n=models.IntegerField(verbose_name="点赞数")

    # member对象
    mid=models.CharField(max_length=30,verbose_name="用户编号")
    uname=models.CharField(max_length=20,verbose_name="用户名称")

    # ctime=models.IntegerField(verbose_name="发布时间")

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

class Comment_hotwords(BaseModel):

    aid = models.ForeignKey(to=Info, to_field="aid", related_name="comment_hotword",db_column='aid', on_delete=models.CASCADE)
    hot_word = models.CharField(max_length=10, verbose_name="评论内容")
    num=models.IntegerField(verbose_name="数量")

    # create_time=models.CharField(max_length=10,verbose_name="创建时间")

    class Meta:
        unique_together = (('aid', 'hot_word'),)
        verbose_name = '评论热词'
        verbose_name_plural = verbose_name

class Danmu_hotwords(BaseModel):

    # cid=models.IntegerField(verbose_name="danmu编号")
    cid = models.ForeignKey(to=Info, to_field="cid", related_name="danmu_hotword",db_column='cid', on_delete=models.CASCADE)
    hot_word = models.CharField(max_length=10, verbose_name="damu内容")
    num=models.IntegerField(verbose_name="数量")

    # update_time = models.CharField(max_length=10, verbose_name="更新时间")
    # create_time = models.CharField(max_length=10, verbose_name="创建时间")

    class Meta:
        unique_together = (('cid', 'hot_word'),)
        verbose_name = '弹幕热词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'cid:{self.cid}-hot_word:{self.hot_word}'

