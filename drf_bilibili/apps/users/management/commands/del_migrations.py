from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.spiders.get_note import GetNoteSpider
from crawl.spiders.get_kol import GetKolSpider


class Command(BaseCommand):
    # 帮助文本, 一般备注命令的用途及如何使用。
    help = "Print Hello World!"

    # 核心业务逻辑，通过options字典接收name参数值，拼接字符串后输出
    def handle(self, *args, **options):
        try:
            import os

            for root, dirs, files in os.walk('.'):
                if 'migrations' in dirs:
                    dir = dirs[dirs.index('migrations')]
                    for root_j, dirs_j, files_j in os.walk(os.path.join(root, dir)):
                        for file_k in files_j:
                            if file_k != '__init__.py':
                                dst_file = os.path.join(root_j, file_k)
                                print('>>> ', dst_file)
                                os.remove(dst_file)
        except:
            print('删除失败')
        finally:
            print('成功删除迁移文件')

