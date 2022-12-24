from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.spiders.get_note import GetNoteSpider


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "爬取用户或者up主笔记信息，可传入mid、aid"

    # 给命令添加一个名为name的参数
    def add_arguments(self, parser):
        parser.add_argument('-mid')
        parser.add_argument('-aid')

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        if options['mid']:
            process.crawl(GetNoteSpider,mid=options['mid'])
        elif options['aid']:
            process.crawl(GetNoteSpider,mid=options['aid'])
        else:
            process.crawl(GetNoteSpider)

        process.start()