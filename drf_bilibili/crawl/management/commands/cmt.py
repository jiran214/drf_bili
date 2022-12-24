from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.spiders.get_comment import GetDanmuCommentSpider


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "爬去用户或者up主评论信息，可传入aid"

    # 给命令添加一个名为name的参数
    def add_arguments(self, parser):
        parser.add_argument('-aid')

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        if options['aid']:
            process.crawl(GetDanmuCommentSpider,mid=options['aid'])
        else:
            process.crawl(GetDanmuCommentSpider)
        process.start()