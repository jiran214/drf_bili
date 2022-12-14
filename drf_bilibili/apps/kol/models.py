from django.db import models

from datetime import datetime
from django.db import models

from utils.model import BaseModel

# Create your models here.
class Info(BaseModel):
    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4


    mid = models.CharField(unique=True,max_length=20,verbose_name="up主编号")
    user_name = models.CharField(max_length=20, verbose_name="")
    sex = models.CharField(max_length=10, verbose_name="性别	男/女/保密")
    face = models.CharField(max_length=200, verbose_name="头像链接") #安全链接
    face_nft = models.IntegerField(null=True, verbose_name="是否nft 头像", choices=((0, "不是nft头像"), (1, "是nft头像")))
    sign = models.CharField(null=True,max_length=100, verbose_name="签名")
    rank_n = models.IntegerField(verbose_name="排名")
    user_level = models.IntegerField(verbose_name="当前等级0-6级")
    silence = models.IntegerField(null=True, verbose_name="封禁状态", choices=((0, "正常"), (1, "被封")))
    # coins	num	硬币数	需要登录(Cookie)

    fans_badge = models.BooleanField(verbose_name="false：无;true：有")

    # official对象
    role_type = models.IntegerField(null=True, verbose_name="认证类型0：无；1279：个人认证；3456：机构认证")
    title = models.CharField(null=True,max_length=100, verbose_name="认证信息 无为空")
    des = models.CharField(null=True,max_length=100, verbose_name="认证备注 无为空")
    is_type = models.IntegerField(null=True, verbose_name="是否认证", choices=((0, "有认证"), (-1, "无认证")))

    # live_room	obj	直播间信息
    birthday = models.CharField(null=True,max_length=50, verbose_name="生日 MM-DD")

    # 最新状态数据
    following = models.IntegerField(default=0, verbose_name="关注")
    follower = models.IntegerField(default=0, verbose_name="粉丝")
    play_view = models.IntegerField(default=0, verbose_name="累计播放量")
    likes = models.IntegerField(default=0, verbose_name="累计获赞量")
    # update_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    # create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    #私密字段# 位置
    #粉丝数据# 扩展字段# 指数

    #作品数据# 作品标签# 互动平均数据

    class Meta:
        verbose_name = '达人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'mid:{self.mid}-username:{self.user_name}'

class Stat(BaseModel):
    # 视频数据

    mid = models.ForeignKey(to=Info, to_field="mid", db_column='mid', related_name="states", on_delete=models.CASCADE)
    following = models.IntegerField(default=0, verbose_name="关注")
    follower = models.IntegerField(default=0, verbose_name="粉丝")
    play_view = models.IntegerField(default=0, verbose_name="累计播放量")
    likes = models.IntegerField(default=0, verbose_name="累计获赞量")
    # create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'mid:{self.mid}-username:{self.play_view}'
    """
    商业数据:报价 是否开直播、带货商品、联系方式、合作品牌、由投放报价
    """
