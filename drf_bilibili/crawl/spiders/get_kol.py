import os
from django.utils import timezone as datetime # 不想大面积修改就这么做

import scrapy
from crawl.settings import redis_conn
from crawl.items import KolItem

class GetKolSpider(scrapy.Spider):
    name = 'get_kol'

    # start_urls = ['http://www.baidu.com/']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mid = getattr(self, 'mid', None)
        self.cookie = redis_conn.get('kol_cookie')

    # 解析粉丝、关注、mid
    def start_requests(self):
        # 爬取笔记作者
        url = 'https://api.bilibili.com/x/relation/stat?vmid='
        while 1:
            if self.mid:
                self.user_id = self.mid
                self.logger.info(f'开始爬取:{self.user_id}')
                yield scrapy.Request(url + str(self.user_id) + '&jsonp=json', callback=self.follow_parse)

                break
            self.user_id = redis_conn.brpop('wait_user_mid')
            self.logger.info(f'开始爬取:{self.user_id}')
            yield scrapy.Request(url + str(self.user_id[1]) + '&jsonp=json', callback=self.follow_parse)

    def follow_parse(self, response):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
            'cookie': self.cookie,
            'authority': 'api.bilibili.com'
        }
        info = response.json()

        user_item = KolItem()
        follower = info['data']['follower']
        following = info['data']['following']
        mid = info['data']['mid']

        user_item['follower'] = follower
        user_item['following'] = following
        user_item['mid'] = mid
        new_url = 'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp'
        yield scrapy.Request(new_url, callback=self.view_parse, headers=self.headers, meta={'user_item': user_item})

    # 解析播放、阅读、喜欢
    def view_parse(self, response):
        # todo 对响应对象的状态检查
        info = response.json()
        play_view = info['data']['archive']['view']
        read_view = info['data']['article']['view']
        likes = info['data']['likes']

        user_item = response.meta['user_item']
        user_item['play_view'] = play_view
        # user_item['read_view'] = read_view
        user_item['likes'] = likes
        mid = response.meta['user_item']['mid']
        new_url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(mid)
        # yield user_item
        yield scrapy.Request(new_url, callback=self.kol_parse, headers=self.headers, meta={'user_item': user_item})

    # 解析kol基本信息
    def kol_parse(self, response):
        filed_map = {
            'mid': 'mid',
            'user_name': 'name',
            'sex': 'sex',
            'face': 'face',
            'face_nft': 'face_nft',
            'sign': 'sign',
            'rank_n': 'rank',
            'user_level': 'level',
            'silence': 'silence',
            'fans_badge': 'fans_badge',
            'birthday': 'birthday'
        }
        filed_offical_map = {
            'role_type': 'role',
            'title': 'title',
            'des': 'desc',
            'is_type': 'type'
        }
        user_item = response.meta['user_item']
        info = response.json()['data']

        for filed, attr in filed_map.items():
            user_item[filed] = info.get(attr)

        for filed, attr in filed_offical_map.items():
            user_item[filed] = info['official'].get(attr)
        from django.utils import timezone
        user_item['update_time']=timezone.datetime.now()
        # if not user_item['sign']:
        #     user_item['sign']='该用户没有签名'
        user_name=user_item['user_name']
        self.logger.info(f'{self.user_id}-{user_name}爬取结束')
        yield user_item
