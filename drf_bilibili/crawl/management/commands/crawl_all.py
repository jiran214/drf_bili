from django.core.management import call_command
from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from crawl.spiders.get_mid import GetMidSpider
from crawl.spiders.get_kol import GetKolSpider
from crawl.spiders.get_note import GetNoteSpider
from crawl.spiders.get_comment import GetDanmuCommentSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "爬去用户或者up主信息，可传入mid"
    scope = 'all'

    # 给命令添加一个名为name的参数
    def add_arguments(self, parser):
        parser.add_argument('-mid')
        parser.add_argument('-aid')

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        # process = CrawlerProcess(get_project_settings())
        call_command('mid_from_channel')
        call_command('kol')
        call_command('note')
        call_command('cmt')

        # process.start()

    def get_class(self):
        from werkzeug.utils import import_string, find_modules
        for module_string in find_modules('crawl.spiders'):
            module = import_string(module_string)
            class_string = module_string.split('.')[-1].capitalize() + 'Spider'
            spider_class = getattr(module, class_string)
            print(spider_class)
