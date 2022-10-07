import scrapy
from crawl.items import CommentItem, DanmuItem
from crawl.settings import redis_conn

import re, datetime


class GetDanmuCommentSpider(scrapy.Spider):
    """
    爬取笔记弹幕和评论
    """
    name = 'get_danmu_comment'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
        # 'referer': 'https://www.bilibili.com/',
    }

    # start_urls = ['http://www.baidu.com/']

    cookie = {
        'cookies': "buvid3=291FE13E-2DA3-591C-20AA-C29ACE40718F68927infoc; b_nut=1660481067; buvid4=3153120C-9D38-EF44-26EE-C602D23D60E768927-022081420-cduZ3OaNjcCVwO2g23YSkw==; i-wanna-go-back=-1; _uuid=DB2EA38F-E5310-C721-B354-A310C12EFBE6772442infoc; buvid_fp_plain=undefined; DedeUserID=410282523; DedeUserID__ckMd5=0f009d0a30b0f8dc; hit-dyn-v2=1; b_ut=5; LIVE_BUVID=AUTO5116604849511857; rpdid=|(um~k)J)lmJ0J'uYY|R)luu); nostalgia_conf=-1; CURRENT_BLACKGAP=0; fingerprint3=afdb02d98c3d3e2641b19d395113f230; blackside_state=1; is-2022-channel=1; SESSDATA=36c2850f,1677744238,99fbd*91; bili_jct=646547de491a4e7c0919a3a16f876712; sid=6szqc7nc; go_old_video=1; fingerprint=9ee78a70b93c610542445b4445bd15e2; CURRENT_QUALITY=80; buvid_fp=9ee78a70b93c610542445b4445bd15e2; CURRENT_FNVAL=16; PVID=2; b_lsid=BBC1E793_183B1EC7AF0; bp_video_offset_410282523=714250510297727000; innersign=1", }
    PAGE = 1  # 评论页数
    RECENT_MONTHS = 3  # 最近几周的弹幕
    DANMU_LIMIT = 1  # 最多爬取几天弹幕

    def start_requests(self):
        # redis
        while 1:
            self.aid = redis_conn.brpop('wait_aid')[1]
            self.cid = redis_conn.brpop('wait_cid')[1]

            self.logger.info(f'开始爬取aid:{self.aid}评论')
            # 爬取视频评论
            comment_url = "https://api.bilibili.com/x/v2/reply/main?mode=3&next=%s&oid=%s&plat=1&type=1"
            for p in range(self.PAGE):
                # pass
                yield scrapy.Request(url=comment_url % (p + 1, str(self.aid)), callback=self.comment_parse,
                                     headers=self.headers)

            # self.logger.info(f'开始爬取cid:{self.cid}弹幕')
            # 爬取视频弹幕
            # date = datetime.date.today()
            # for d in range(self.RECENT_MONTHS):
            #     date = date - datetime.timedelta(days=30)
            #     # print(date)
            #     dammu_date_url = 'http://api.bilibili.com/x/v2/dm/history/index?type=1&oid=%s&month=%s'
            #     # print(dammu_date_url % (str(self.cid), date.strftime('%Y-%m')))
            #     yield scrapy.Request(dammu_date_url % (str(self.cid), str(date)),
            #                          callback=self.danmu_date_parse,
            #                          headers=self.headers, cookies=self.cookie, meta={'cid': self.cid})

    """
    Comment unsupported operand type
    """

    def comment_parse(self, response):
        info = response.json()

        comments = info['data']['replies']
        if info['code'] == 0 and comments:
            for comment in comments:
                comment_item = CommentItem()
                comment_item['aid'] = comment['oid']
                comment_item['content'] = comment['content']['message']
                comment_item['like_n'] = comment['like']
                comment_item['mid'] = comment['mid']
                comment_item['uname'] = comment['member']['uname']
                comment_item['ctime'] = comment['ctime']

                self.logger.info(f'aid:{self.aid}评论爬取完毕')
                yield comment_item
        else:
            self.logger.warn(f'aid:{self.aid}评论未爬取到')

    """
    Dan mu
    """

    def danmu_date_parse(self, response):
        # info = response.json()
        info = response.json()
        code = info['code']
        if code == 0:
            cid = response.meta['cid']
            for d in info['data'][:self.DANMU_LIMIT]:
                dammu_url = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=' + str(cid) + '&date=' + d
                yield scrapy.Request(url=dammu_url, callback=self.danmu_parse, headers=self.headers,cookies=self.cookie,
                                     meta={'cid': cid, 'date': d})
        else:
            self.logger.warn(f'code:{code}cid:{self.cid}弹幕未爬取到')

    def danmu_parse(self, response):

        cid = response.meta['cid']
        date = response.meta['date']
        danmus = response.body.decode('utf-8', 'ignore')
        ex = '[\u4e00-\u9fa5]+'
        danmus = re.findall(ex, danmus)
        for danmu in danmus:
            danmu_item = DanmuItem()
            danmu_item['cid'] = cid
            danmu_item['content'] = danmu
            danmu_item['ctime'] = date
            print(danmu)

            self.logger.info(f'cid:{self.cid}弹幕爬取完毕')
            yield danmu_item
