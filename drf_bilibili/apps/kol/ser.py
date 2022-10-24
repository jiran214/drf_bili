import datetime
import time

from django.db.models import Avg
from rest_framework import serializers
from apps.kol.models import Info as kol_info, Stat
from apps.note.models import Info as note_info


class NoteInfoSer(serializers.ModelSerializer):
    class Meta:
        model = note_info
        fields = '__all__'


class KolInfoSer(serializers.ModelSerializer):
    # notes=NoteInfoSer(many=True,read_only=True)
    class Meta:
        model = kol_info
        fields = '__all__'


class KolStatSer(serializers.ModelSerializer):
    # notes=NoteInfoSer(many=True,read_only=True)
    class Meta:
        model = Stat
        fields = ['follower', 'likes', 'play_view', 'create_time']


class KolDetailSer(serializers.ModelSerializer):
    # 近十天笔记数据播放
    # notes = NoteInfoSer(many=True, read_only=True)

    recent_data = serializers.SerializerMethodField()
    states = KolStatSer(many=True)

    # = serializers.SerializerMethodField()

    class Meta:
        model = kol_info
        fields = ['mid', 'recent_data', 'states']

    def get_recent_data(self, obj):
        # 近三十天笔记的平均数据
        # days_30 = datetime.datetime.now().date() - datetime.timedelta(days=30)
        ts = time.time() - 86400 * 30  # 30天前时间戳# 30天前
        fileds = ('view_n', 'reply', 'favorite', 'like_n', 'coin', 'share')
        avg_data = obj.notes.filter(pubdate__gte=ts).aggregate(*(Avg(filed) for filed in fileds))  # 查询集合的全部对象聚合

        # 近个天笔记的三连、播放数据 折线图
        quertset = obj.notes.order_by('-pubdate')[:10]
        ten_notes = []
        fileds = ('view_n', 'favorite', 'like_n', 'coin', 'pubdate', 'name', 'title')
        ten_notes = {}
        for note in quertset:
            for filed in fileds:
                ten_notes.setdefault('ten_' + filed, []).append(getattr(note, filed, 0))

        data = {
            'avgs': avg_data,
            'ten_notes': ten_notes
        }

        return data

    def to_representation(self, value):
        # 调用父类获取当前序列化数据，value代表每个对象实例obj
        data = super().to_representation(value)
        # 对序列化数据做修改，添加新的数据

        """三连、互动变化趋势图"""
        draw_data = {'ins': {'follower_y': [],
                             "likes_y": [],
                             "play_view_y": [],
                             "ctime": []},
                     'all': {'follower_y': [],
                             "likes_y": [],
                             "play_view_y": [],
                             "ctime": []}}

        fileds = ("follower", "likes", "play_view",)

        states = data['states']

        last = {}
        for stat in states:
            ctime = stat['create_time'][:10]
            if ctime not in draw_data['all']['ctime']:
                draw_data['all']['ctime'].append(ctime)
                if last:
                    print(ctime)
                    # 第一次不创建时间
                    draw_data['ins']['ctime'].append(ctime)
                for filed in fileds:
                    v = stat[filed]
                    if filed in last:
                        draw_data['ins'][filed + '_y'].append(v - last[filed])

                    draw_data['all'][filed + '_y'].append(v)
                    last[filed] = v

        data['states'] = draw_data

        return data


class kolMessageSer(serializers.Serializer):
    # danmu_hotwords = serializers.SerializerMethodField()
    comment_hotwords = serializers.SerializerMethodField()

    class Meta:
        model = kol_info

    def get_comment_hotwords(self, obj):

        queryset = obj.notes.all()

        data = {}
        for note in queryset:
            comment_hotword = note.comment_hotword

            if comment_hotword.exists():
                for c in comment_hotword:
                    word = c['hot_word']
                    if word not in data:
                        data[word] = 0
                    data[word] += c['num']

        if data:
            data = sorted(data.items(), key=lambda item: item[1], reverse=True)[:20]  # 排序

            unzip_data = zip(*data)
            after_data = {}
            after_data['hot_word'] = unzip_data[0]
            after_data['num'] = unzip_data[1]

            return after_data
