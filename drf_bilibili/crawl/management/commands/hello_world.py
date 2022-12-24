from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.spiders.get_note import GetNoteSpider
from crawl.spiders.get_kol import GetKolSpider


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "Print Hello World!"

    # 给命令添加一个名为name的参数
    def add_arguments(self, parser):
        parser.add_argument('name')

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        msg = 'Hello World ! ' + options['name']
        self.stdout.write(msg)

        process = CrawlerProcess(get_project_settings())
        process.crawl(GetKolSpider,mid=options['name'])
        process.start()