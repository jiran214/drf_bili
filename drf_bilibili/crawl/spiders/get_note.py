import os

import time

import scrapy

from crawl.items import NoteItem
from crawl.settings import redis_conn, LOG_FILE
from scrapy import Request
from django.utils import timezone as datetime

class GetNoteSpider(scrapy.Spider):
    """
    从kol主页获取最新笔记
    """
    name = 'get_note'
    allowed_domains = ['www.baidu.com', 'api.bilibili.com']

    # user_id = '2026561407'
    headers = {
        'Cookie': "buvid3=291FE13E-2DA3-591C-20AA-C29ACE40718F68927infoc; b_nut=1660481067; buvid4=3153120C-9D38-EF44-26EE-C602D23D60E768927-022081420-cduZ3OaNjcCVwO2g23YSkw==; i-wanna-go-back=-1; _uuid=DB2EA38F-E5310-C721-B354-A310C12EFBE6772442infoc; buvid_fp_plain=undefined; DedeUserID=410282523; DedeUserID__ckMd5=0f009d0a30b0f8dc; hit-dyn-v2=1; b_ut=5; LIVE_BUVID=AUTO5116604849511857; rpdid=|(um~k)J)lmJ0J'uYY|R)luu); nostalgia_conf=-1; CURRENT_BLACKGAP=0; fingerprint3=afdb02d98c3d3e2641b19d395113f230; blackside_state=1; is-2022-channel=1; SESSDATA=36c2850f,1677744238,99fbd*91; bili_jct=646547de491a4e7c0919a3a16f876712; sid=6szqc7nc; fingerprint=5eaeda73cb80d727cd671bf00d4b42a0; buvid_fp=5eaeda73cb80d727cd671bf00d4b42a0; CURRENT_QUALITY=80; PVID=1; innersign=0; CURRENT_FNVAL=16; bp_video_offset_410282523=704295123925598200; b_lsid=2B6A101E5_18327D2FBA5",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
    }

    def start_requests(self):
        while 1:
            self.user_id = redis_conn.brpop('wait_note_mid')[1]
            self.logger.info(f'开始爬取:{self.user_id}的笔记')

            url = 'http://api.bilibili.com/x/space/arc/search?mid=%s&ps=20&pn=1&order=pubdate' % self.user_id  # order:click播放
            # time.sleep(0.3)
            yield Request(url=url, callback=self.note_list_parse, headers=self.headers)

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
            note_item[filed] = result['stat'].get(attr)
        note_item['update_time'] = datetime.datetime.now()
        note_item['des'] = note_item['des'][:300].replace('\n',' ')

        # print('名字:', note_item['aid'], 'note数据爬取结束')
        aid=note_item['aid']
        self.logger.info(f'aid:{self.user_id}-aid:{aid}爬取结束')

        yield note_item
