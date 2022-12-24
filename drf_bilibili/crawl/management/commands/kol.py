from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.spiders.get_kol import GetKolSpider


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "爬取用户或者up主信息，可传入mid"

    # 给命令添加一个名为name的参数
    def add_arguments(self, parser):
        parser.add_argument('-mid')

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        if options['mid']:
            process.crawl(GetKolSpider,mid=options['mid'])
        else:
            process.crawl(GetKolSpider)
        process.start()