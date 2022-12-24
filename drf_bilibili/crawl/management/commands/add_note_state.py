from datetime import timedelta

from django.core.management.base import BaseCommand

from apps.kol.models import Info as Kol
from apps.note import models as Note
from django.utils import timezone
import random

filed_map = ('view_n', 'danmaku', 'reply', 'reply', 'coin', 'share', 'like_n', 'favorite')


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "为up主或者笔记添加指定数目的模拟数据!"

    # 给命令添加一个名为name的参数
    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self._dict_data = {}

    def add_arguments(self, parser):
        """
        aid 和 aidNum 不能同时传
        """
        parser.add_argument('-aid', nargs='+')
        parser.add_argument('-aidNum')  # 需要模拟的笔记数
        parser.add_argument('addNum')  # 需要添加的状态数

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        aids, num, aidNum = options['aid'], int(options['addNum']), options['aidNum']

        if not aids:
            aids = list(Note.Info.objects.values_list('aid', flat=True))
            aids = random.choices(aids, k=int(aidNum or 5))

        if aidNum and num:
            self.stdout.write('aid 和 aidNum 不能同时传 ')

        for aid in aids:
            note = Note.Info.objects.get(aid=aid)
            # 初始化数据
            self._dict_data = {filed: note.__dict__[filed] for filed in filed_map}
            # self._dict_data.pop('_state')
            self._dict_data['aid'] = note

            try:
                for n in range(num):
                    self.update_data()
                    date = timezone.now() - timedelta(days=(num - n) * 2)
                    print(date)
                    self._dict_data['create_time'] = date
                    Note.Stat.objects.create(**self._dict_data)
                self._dict_data = None
                self.stdout.write(f'>>{aid}插入数据成功')
            except Exception as e:
                self.stdout.write(f'>>{aid}插入数据失败:error{e}')

    def update_data(self):
        ran = random.random() * 0.5 + 1
        for filed in filed_map:
            self._dict_data[filed] = int(self._dict_data[filed] * ran)
