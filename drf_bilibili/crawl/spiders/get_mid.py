from datetime import datetime, timedelta

import scrapy
from crawl.settings import redis_conn
from scrapy import Request


class GetMidSpider(scrapy.Spider):
    """
    从频道拿到mid
    """
    name = 'get_mid'

    # start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        '''
                    名称   代号    tid/rid
                    宅舞	    otaku	    20
                    单机游戏	stand_alone	17
                    电子竞技	esports	171
                    人文历史	humhistory  228
                    科学科普	science	201
                    财经商业	business	207
                    校园学习	campus	208
                    数码(原手机平板)	digital	95
                    健身	aerobics	164
                    汽车生活	life	176
                    汽车文化	culture	224
                    搞笑	funny	138
                    日常	daily	21
                    手工	handmake	161
                    家具房产            239
                    美食制作   	make 76
                    美食侦探	detective   212
                    美食测评	measurement	213
                    喵星人	cat	218
                    汪星人	dog	219
                    鬼畜（主分区）	kichiku	119
                    时尚（主分区）	fashion	155
                    美妆	makeup	157
                    服饰	clothing	158
                    综艺	variety	71
                    影视杂谈	cinecism	182
        '''
        cate_ids = {
            '20': 20, '17': 20, '171': 20,
            '228': 20, '201': 30, '207': 25, '208': 15,
            '95': 50, '164': 40,
            '176': 10, '224': 10,
            '138': 50, '21': 50, '161': 20,
            '239': 30,
            '76': 50, '212': 50, '213': 50,
            '218': 30, '219': 30,
            '119': 40, '155': 50, '157': 50,
            '158': 50, '71': 40, '182': 40,
        }
        for cate_id, max_pages in cate_ids.items():
            for page in range(1, max_pages + 1):
                days = 1  # 爬取最近天数
                order_type = 'click'  # order_type: scores-评论数, click-播放量
                ps = 20
                start_date = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')
                end_date = datetime.now().strftime('%Y%m%d')
                url = 'https://s.search.bilibili.com/cate/search?search_type=video&view_type=hot_rank&order=%s&cate_id' \
                      '=%s&page=%s&pagesize=%s&time_from=%s&time_to=%s' \
                      % (order_type,cate_id, page,str(ps), start_date, end_date)

                yield Request(
                    url, meta={'page': page, 'cate_id': cate_id}, callback=self.user_id_parse
                )

                if page==3:
                    break

    def user_id_parse(self, response):
        resp_dict = response.json()
        for note_dict in resp_dict['result']:
            user_id = note_dict['mid']
            self.logger.info(f'{user_id}存入redis')
            redis_conn.lpush('wait_user_mid', user_id)
