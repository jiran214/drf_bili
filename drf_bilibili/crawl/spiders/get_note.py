import os
import random

import time

import scrapy

from crawl.items import NoteItem
from crawl.settings import redis_conn
from scrapy import Request
from django.utils import timezone as datetime

class GetNoteSpider(scrapy.Spider):
    """
    从kol主页获取最新笔记
    """
    name = 'get_note'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mid = getattr(self, 'mid', None)
        self.aid = getattr(self, 'aid', None)
        self.allowed_domains = ['www.baidu.com', 'api.bilibili.com']
        self.cookie = redis_conn.get('kol_cookie')
        self.headers = {
            # 'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
        }

    def start_requests(self):
        url = 'http://api.bilibili.com/x/space/arc/search?mid=%s&ps=20&pn=1&order=pubdate'  # order:click播放

        while 1:
            if self.aid:
                note_tag_url = 'http://api.bilibili.com/x/tag/archive/tags?aid=%s'
                yield Request(url=note_tag_url % self.aid, meta={"note_id": self.aid},
                              callback=self.tag_parse)
                break

            if self.mid:
                self.user_id = self.mid
                self.logger.info(f'开始爬取:{self.user_id}的笔记')
                yield Request(url=url % self.user_id, callback=self.note_list_parse, headers=self.headers)
                break

            self.user_id = redis_conn.brpop('wait_note_mid')[1]
            self.logger.info(f'开始爬取:{self.user_id}的笔记')
            yield Request(url=url % self.user_id, callback=self.note_list_parse, headers=self.headers)

    def note_list_parse(self, response):
        list_dict = response.json()['data']['list']['vlist']
        for video in list_dict:
            note_id = video['aid']
            note_tag_url = 'http://api.bilibili.com/x/tag/archive/tags?aid=%s'
            yield Request(url=note_tag_url % note_id, meta={"note_id": note_id},
                          callback=self.tag_parse)

    # 为视频添加标签
    def tag_parse(self, response):
        note_id = response.meta["note_id"]
        resp_dict = response.json()
        tag_list = [item['tag_name'] for item in resp_dict['data']]

        note_item = NoteItem()
        tag = ';'.join(tag_list)
        note_item['tag'] = tag

        url = 'http://api.bilibili.com/x/web-interface/view?aid=%s' % note_id
        yield Request(url, callback=self.detail_parse, meta={"note_item": note_item}, headers=self.headers)

    def detail_parse(self, response):
        print(response.status)
        note_item = response.meta['note_item']
        result = response.json()['data']
        filed_map = {
            'aid': 'aid',
            'bvid': 'bvid',
            'cid': 'cid',
            'copyright': 'copyright',
            'ctime': 'ctime',
            'des': 'desc',
            'duration': 'duration',
            'dynamic': 'dynamic',

            'pic': 'pic',
            'pub_location': 'pub_location',
            'pubdate': 'pubdate',
            'short_link': 'short_link',
            'tid': 'tid',
            'title': 'title',
            'tname': 'tname'
            # 'create_time': 'create_time'
        }
        filed_owner_map = {
            'mid': 'mid',
            'name': 'name',
            'face': 'face',
        }
        filed_stat_map = {
            'view_n': 'view',
            'danmaku': 'danmaku',
            'reply': 'reply',
            'favorite': 'favorite',
            'coin': 'coin',
            'share': 'share',
            'like_n': 'like'
        }

        for filed, attr in filed_map.items():
            note_item[filed] = result.get(attr)
        for filed, attr in filed_owner_map.items():
            note_item[filed] = result['owner'].get(attr)
        for filed, attr in filed_stat_map.items():
            note_item[filed] = int(result['stat'].get(attr))
        note_item['update_time'] = datetime.datetime.now()
        note_item['des'] = note_item['des'][:300].replace('\n', ' ')

        # print('名字:', note_item['aid'], 'note数据爬取结束')
        aid = note_item['aid']
        # self.logger.info(f'aid:{self.user_id}-aid:{aid}爬取结束')

        yield note_item
