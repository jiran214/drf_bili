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


class KolDetailSer(serializers.ModelSerializer):
    # 近十天笔记数据播放
    notes = NoteInfoSer(many=True, read_only=True)

    recent_data = serializers.SerializerMethodField()

    # = serializers.SerializerMethodField()

    class Meta:
        model = kol_info
        fields = ['mid', 'notes', 'recent_data']

    def get_recent_data(self, obj):
        # 近三十天笔记的平均数据
        # days_30 = datetime.datetime.now().date() - datetime.timedelta(days=30)
        ts = time.time() - 86400 * 30  # 30天前时间戳# 30天前
        fileds = ('view_n', 'reply', 'favorite', 'like_n', 'coin', 'share')
        # 查询集合的全部对象聚合
        query_set = obj.notes.filter(pubdate__gte=ts).aggregate(*(Avg(filed) for filed in fileds))
        # follower = obj.mid.follower
        data = {
            'avgs': query_set
        }
        return data


class KolStatSer(serializers.ModelSerializer):
    # notes=NoteInfoSer(many=True,read_only=True)
    class Meta:
        model = Stat
        fields = '__all__'
