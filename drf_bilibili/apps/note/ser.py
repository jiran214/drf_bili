from rest_framework import serializers

# from note.models import VideoInfo, Note, NoteAddInfo, Comment, DetailInfo
from apps.note.models import Info, Danmu, Comment, Danmu_hotwords, Comment_hotwords, Stat


class NoteDanmuSer(serializers.ModelSerializer):
    class Meta:
        model = Danmu
        fields = '__all__'


class CommentHotWordsSer(serializers.ModelSerializer):
    class Meta:
        model = Comment_hotwords
        fields = '__all__'


class DanmuHotWordsSer(serializers.ModelSerializer):
    class Meta:
        model = Danmu_hotwords
        fields = ['hot_word', 'num']


class NoteCommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NoteInfoSer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        depth = 1


class NoteDetailSer(serializers.ModelSerializer):
    danmus = NoteDanmuSer(many=True)
    comments = NoteCommentSer(many=True)
    danmu_hotword = DanmuHotWordsSer(many=True)
    comment_hotword = CommentHotWordsSer(many=True)

    # 互动粉丝比 # 三连粉丝比
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['aid', 'mid', 'danmus', 'comments', 'danmu_hotword', 'comment_hotword', 'percent']
        # fields = '__all__'
        depth = 1

    def get_percent(self, obj):
        follower = obj.mid.follower
        fileds = ('view_n', 'reply', 'favorite', 'coin', 'like_n')

        data = {filed + '_percent': '{:.2%}'.format(getattr(obj, filed, 0) / follower) for filed in fileds}

        return data


class NoteStatSer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'
        # depth = 1
