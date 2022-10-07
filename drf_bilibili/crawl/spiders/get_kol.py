import os
from django.utils import timezone as datetime # 不想大面积修改就这么做

import scrapy
from crawl.settings import redis_conn, LOG_FILE
from crawl.items import KolItem

class GetKolSpider(scrapy.Spider):
    name = 'get_kol'

    # start_urls = ['http://www.baidu.com/']

    # 解析粉丝、关注、mid
    def start_requests(self):
        # 爬取笔记作者
        while 1:
            self.user_id = redis_conn.brpop('wait_user_mid')
            self.logger.info(f'开始爬取:{self.user_id}')
            url = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(self.user_id[1]) + '&jsonp=json'
            yield scrapy.Request(url, callback=self.follow_parse)

    def follow_parse(self, response):
        self.headers = {
            'Cookie': "buvid3=291FE13E-2DA3-591C-20AA-C29ACE40718F68927infoc; b_nut=1660481067; buvid4=3153120C-9D38-EF44-26EE-C602D23D60E768927-022081420-cduZ3OaNjcCVwO2g23YSkw==; i-wanna-go-back=-1; _uuid=DB2EA38F-E5310-C721-B354-A310C12EFBE6772442infoc; buvid_fp_plain=undefined; DedeUserID=410282523; DedeUserID__ckMd5=0f009d0a30b0f8dc; hit-dyn-v2=1; b_ut=5; LIVE_BUVID=AUTO5116604849511857; rpdid=|(um~k)J)lmJ0J'uYY|R)luu); nostalgia_conf=-1; CURRENT_BLACKGAP=0; fingerprint3=afdb02d98c3d3e2641b19d395113f230; blackside_state=1; is-2022-channel=1; SESSDATA=36c2850f,1677744238,99fbd*91; bili_jct=646547de491a4e7c0919a3a16f876712; sid=6szqc7nc; fingerprint=5eaeda73cb80d727cd671bf00d4b42a0; buvid_fp=5eaeda73cb80d727cd671bf00d4b42a0; CURRENT_QUALITY=80; PVID=1; innersign=0; CURRENT_FNVAL=16; bp_video_offset_410282523=704295123925598200; b_lsid=2B6A101E5_18327D2FBA5",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
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

        info = response.json()
        # print(info)
        play_view = info['data']['archive']['view']
        read_view = info['data']['article']['view']
        likes = info['data']['likes']

        user_item = response.meta['user_item']
        user_item['play_view'] = play_view
        # user_item['read_view'] = read_view
        user_item['likes'] = likes
        mid = response.meta['user_item']['mid']
        new_url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(mid) + '&jsonp=jsonp'
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

        user_item['update_time']=datetime.datetime.now()
        # if not user_item['sign']:
        #     user_item['sign']='该用户没有签名'
        user_name=user_item['user_name']
        self.logger.info(f'{self.user_id}-{user_name}爬取结束')
        yield user_item
