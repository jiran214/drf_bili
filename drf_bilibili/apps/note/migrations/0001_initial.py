# Generated by Django 4.0.7 on 2022-10-06 08:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


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
                ('aid', models.IntegerField(unique=True, verbose_name='视频aid')),
                ('bvid', models.CharField(max_length=20, unique=True, verbose_name='稿件ID')),
                ('cid', models.IntegerField(null=True, unique=True, verbose_name='视频cid')),
                ('copyright', models.IntegerField(choices=[(1, '原创'), (2, '转载')], null=True)),
                ('ctime', models.IntegerField(verbose_name='投稿时间')),
                ('des', models.CharField(max_length=300, verbose_name='视频描述')),
                ('duration', models.IntegerField(verbose_name='视频总时长')),
                ('dynamic', models.CharField(max_length=500, verbose_name='视频同步发布的的动态的文字内容')),
                ('tag', models.CharField(max_length=100, null=True, verbose_name='标签')),
                ('name', models.CharField(max_length=50, verbose_name='up主名字')),
                ('face', models.CharField(max_length=100, verbose_name='up主头像')),
                ('pic', models.CharField(max_length=100, verbose_name='封面')),
                ('pub_location', models.CharField(max_length=20, null=True, verbose_name='地址')),
                ('pubdate', models.IntegerField(verbose_name='发布时间')),
                ('short_link', models.CharField(max_length=100, null=True, verbose_name='视频链接')),
                ('tid', models.IntegerField(verbose_name='分区编号')),
                ('title', models.CharField(max_length=100, verbose_name='视频标题')),
                ('tname', models.CharField(max_length=10, verbose_name='二级分区')),
                ('view_n', models.IntegerField(default=0, verbose_name='播放数')),
                ('danmaku', models.IntegerField(default=0, verbose_name='弹幕数')),
                ('reply', models.IntegerField(default=0, verbose_name='评论数')),
                ('favorite', models.IntegerField(default=0, verbose_name='收藏数')),
                ('coin', models.IntegerField(default=0, verbose_name='投币数')),
                ('share', models.IntegerField(default=0, verbose_name='分享数')),
                ('like_n', models.IntegerField(default=0, verbose_name='点赞数')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='添加时间')),
                ('mid', models.ForeignKey(db_column='mid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='notes', to='kol.info', to_field='mid')),
            ],
            options={
                'verbose_name': '笔记',
                'verbose_name_plural': '笔记',
            },
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_n', models.IntegerField(default=0, verbose_name='播放数')),
                ('danmaku', models.IntegerField(default=0, verbose_name='弹幕数')),
                ('reply', models.IntegerField(default=0, verbose_name='评论数')),
                ('favorite', models.IntegerField(default=0, verbose_name='收藏数')),
                ('coin', models.IntegerField(default=0, verbose_name='投币数')),
                ('share', models.IntegerField(default=0, verbose_name='分享数')),
                ('like_n', models.IntegerField(default=0, verbose_name='点赞数')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('aid', models.ForeignKey(db_column='aid', on_delete=django.db.models.deletion.CASCADE, related_name='states', to='note.info', to_field='aid')),
            ],
            options={
                'verbose_name': '状态',
                'verbose_name_plural': '状态',
            },
        ),
        migrations.CreateModel(
            name='Danmu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='弹幕内容')),
                ('ctime', models.CharField(max_length=10, verbose_name='发布时间')),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, related_name='danmus', to='note.info', to_field='cid')),
            ],
            options={
                'verbose_name': '弹幕',
                'verbose_name_plural': '弹幕',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('like_n', models.IntegerField(verbose_name='点赞数')),
                ('mid', models.CharField(max_length=30, verbose_name='用户编号')),
                ('uname', models.CharField(max_length=20, verbose_name='用户名称')),
                ('ctime', models.IntegerField(verbose_name='发布时间')),
                ('aid', models.ForeignKey(db_column='aid', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='note.info', to_field='aid')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Danmu_hotwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_word', models.CharField(max_length=10, verbose_name='damu内容')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('update_time', models.CharField(max_length=10, verbose_name='更新时间')),
                ('create_time', models.CharField(max_length=10, verbose_name='创建时间')),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, related_name='danmu_hotword', to='note.info', to_field='cid')),
            ],
            options={
                'verbose_name': '弹幕热词',
                'verbose_name_plural': '弹幕热词',
                'unique_together': {('cid', 'hot_word')},
            },
        ),
        migrations.CreateModel(
            name='Comment_hotwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_word', models.CharField(max_length=10, verbose_name='评论内容')),
                ('num', models.IntegerField(verbose_name='数量')),
                ('create_time', models.CharField(max_length=10, verbose_name='创建时间')),
                ('aid', models.ForeignKey(db_column='aid', on_delete=django.db.models.deletion.CASCADE, related_name='comment_hotword', to='note.info', to_field='aid')),
            ],
            options={
                'verbose_name': '评论热词',
                'verbose_name_plural': '评论热词',
                'unique_together': {('aid', 'hot_word')},
            },
        ),
    ]
