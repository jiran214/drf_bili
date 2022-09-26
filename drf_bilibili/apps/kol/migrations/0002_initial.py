# Generated by Django 4.1.1 on 2022-09-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField(unique=True, verbose_name='up主编号')),
                ('user_name', models.CharField(max_length=20, verbose_name='')),
                ('sex', models.CharField(max_length=10, verbose_name='性别\t男/女/保密')),
                ('face', models.CharField(max_length=200, verbose_name='头像链接')),
                ('face_nft', models.IntegerField(choices=[(0, '不是nft头像'), (1, '是nft头像')], null=True, verbose_name='是否nft 头像')),
                ('sign', models.CharField(max_length=100, null=True, verbose_name='签名')),
                ('rank_n', models.IntegerField(verbose_name='排名')),
                ('user_level', models.IntegerField(verbose_name='当前等级0-6级')),
                ('silence', models.IntegerField(choices=[(0, '正常'), (1, '被封')], null=True, verbose_name='封禁状态')),
                ('fans_badge', models.BooleanField(verbose_name='false：无;true：有')),
                ('role_type', models.IntegerField(null=True, verbose_name='认证类型0：无；1279：个人认证；3456：机构认证')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='认证信息 无为空')),
                ('des', models.CharField(max_length=100, null=True, verbose_name='认证备注 无为空')),
                ('is_type', models.IntegerField(choices=[(0, '有认证'), (-1, '无认证')], null=True, verbose_name='是否认证')),
                ('birthday', models.CharField(max_length=50, null=True, verbose_name='生日 MM-DD')),
                ('following', models.IntegerField(default=0, verbose_name='关注')),
                ('follower', models.IntegerField(default=0, verbose_name='粉丝')),
                ('play_view', models.IntegerField(default=0, verbose_name='累计播放量')),
                ('likes', models.IntegerField(default=0, verbose_name='累计获赞量')),
            ],
        ),
    ]
