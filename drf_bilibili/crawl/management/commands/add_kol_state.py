from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.kol import models as Kol
from django.utils import timezone
import random

filed_map = ('following', 'follower', 'play_view', 'likes')
class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "为up主或者笔记添加指定数目的模拟数据!"

    # 给命令添加一个名为name的参数
    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self._dict_data = {}

    def add_arguments(self, parser):
        """
        mid 和 midNum 不能同时传
        """
        parser.add_argument('-mid', nargs='+')
        parser.add_argument('-midNum')  # 需要模拟的笔记数
        parser.add_argument('addNum')  # 需要添加的状态数

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        mids, num, midNum = options['mid'], int(options['addNum']), options['midNum']

        if not mids:
            mids = list(Kol.Info.objects.values_list('mid', flat=True))
            mids = random.choices(mids, k=int(midNum or 5))

        if midNum and num:
            self.stdout.write('mid 和 midNum 不能同时传 ')

        for mid in mids:
            kol = Kol.Info.objects.get(mid=mid)
            # 初始化数据
            self._dict_data = {filed: kol.__dict__[filed] for filed in filed_map}
            # self._dict_data.pop('_state')
            try:
                for n in range(num):
                    self.update_data()
                    date = timezone.now() - timedelta(days=(num - n) * 2)
                    self._dict_data['create_time'] = date
                    kol.states.create(**self._dict_data)

                self._dict_data = None
                self.stdout.write(f'>>{mid}插入数据成功')
            except Exception as e:
                self.stdout.write(f'>>{mid}插入数据失败:error{e}')

    def update_data(self):
        ran = random.random() * 0.5 + 1
        for filed in filed_map:
            self._dict_data[filed] = int(self._dict_data[filed] * ran)
