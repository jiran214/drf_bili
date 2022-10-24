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
        fields = ['hot_word', 'num']


class DanmuHotWordsSer(serializers.ModelSerializer):
    class Meta:
        model = Danmu_hotwords
        fields = ['hot_word', 'num']


class NoteCommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NoteInfoSer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()

    class Meta:
        model = Info
        # fields = '__all__'
        exclude = ('tag', 'des')
        depth = 1

    def get_tags(self, obj):
        tags = obj.tag
        data = tags.split(';')
        return data

    def get_desc(self, obj):
        data = des = obj.des
        if len(des) > 50:
            data = des[:50] + '...'
        return data


class NoteStatSer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        exclude = ('aid', 'id')


class NoteDetailSer(serializers.ModelSerializer):
    states = NoteStatSer(many=True)
    # 互动粉丝比 # 三连粉丝比
    percent = serializers.SerializerMethodField()

    # draw_data = serializers.DictField()

    class Meta:
        model = Info
        fields = ['aid', 'percent', 'states']
        # fields = '__all__'
        depth = 1

    def get_percent(self, obj):
        follower = obj.mid.follower
        fileds = ('view_n', 'reply', 'favorite', 'coin', 'like_n')

        data = {filed + '_percent': '{:.2%}'.format(getattr(obj, filed, 0) / follower) for filed in fileds}

        return data

    def to_representation(self, value):
        # 调用父类获取当前序列化数据，value代表每个对象实例obj
        data = super().to_representation(value)
        # 对序列化数据做修改，添加新的数据

        """三连、互动变化趋势图"""
        draw_data = {'ins': {'view_n_y': [],
                             "danmaku_y": [],
                             "reply_y": [],
                             "favorite_y": [],
                             "coin_y": [],
                             "share_y": [],
                             "like_n_y": [],
                             "ctime": []},
                     'all': {'view_n_y': [],
                             "danmaku_y": [],
                             "reply_y": [],
                             "favorite_y": [],
                             "coin_y": [],
                             "share_y": [],
                             "like_n_y": [],
                             "ctime": []}}

        fileds = ("view_n", "danmaku", "reply", "favorite", "coin", "share", "like_n",)

        states = sorted(data['states'], key=lambda o: o['create_time'])

        last = {}
        for stat in states:
            ctime = stat['create_time'][:10]
            if ctime not in draw_data['all']['ctime']:
                draw_data['all']['ctime'].append(ctime)
                if last:
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


class NoteMessageSer(serializers.Serializer):
    # danmu = N
    comments = NoteCommentSer(many=True)
    danmu_hotword = DanmuHotWordsSer(many=True)
    comment_hotword = CommentHotWordsSer(many=True)

    class Meta:
        model = Info
        fields = '__all__'
        # depth = 1

    # def get_comments(self,obj):
    #
    #     queryset= obj.comments
    #
    #     data = {
    #         'comments':queryset
    #     }
    #     print(data)
    #     return data

    # def get_danmu(self,obj):
    #
    #     data = []
    #     return data

    def to_representation(self, value):
        # 调用父类获取当前序列化数据，value代表每个对象实例obj
        data = super().to_representation(value)

        # 对序列化数据做修改，添加新的数据
        fileds = ('danmu_hotword', 'comment_hotword')

        """转换评论 弹幕数据格式"""
        for filed in fileds:
            draw_data = {}
            draw_data['num'] = []
            draw_data['word'] = []

            for d in data[filed]:
                draw_data['num'].append(d['num'])
                draw_data['word'].append(d['hot_word'])

            data[filed] = draw_data

        return data
