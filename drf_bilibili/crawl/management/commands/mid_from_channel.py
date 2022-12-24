from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.spiders.get_mid import GetMidSpider


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "爬取tid下的up主mid"

    # 给命令添加一个名为name的参数
    def add_arguments(self, parser):
        pass

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(GetMidSpider)

        process.start()