import scrapy
from crawl.items import CommentItem, DanmuItem
from crawl.settings import redis_conn


class GetDanmuCommentSpider(scrapy.Spider):
    """
    爬取笔记弹幕和评论
    """
    cookie = redis_conn.get('kol_cookie')
    name = 'get_comment'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
        # 'referer': 'https://www.bilibili.com/',
        'cookies': cookie,
    }

    # start_urls = ['http://www.baidu.com/']

    PAGE = 1  # 评论页数
    RECENT_MONTHS = 3  # 最近几周的弹幕
    DANMU_LIMIT = 1  # 最多爬取几天弹幕

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.aid = getattr(self, 'aid', None)

    def start_requests(self):
        # redis
        while 1:
            comment_url = "https://api.bilibili.com/x/v2/reply/main?mode=3&next=%s&oid=%s&plat=1&type=1"
            if self.aid:
                for p in range(self.PAGE):
                    yield scrapy.Request(url=comment_url % (p + 1, str(self.aid)), callback=self.comment_parse,
                                     headers=self.headers)
                break

            self.aid = redis_conn.brpop('wait_aid')[1]
            self.logger.info(f'开始爬取aid:{self.aid}评论')
            # 爬取视频评论
            for p in range(self.PAGE):
                yield scrapy.Request(url=comment_url % (p + 1, str(self.aid)), callback=self.comment_parse,
                                     headers=self.headers)

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
                # comment_item['ctime'] = comment['ctime']

                self.logger.info(f'aid:{self.aid}评论爬取完毕')
                yield comment_item
        else:
            self.logger.warn(f'aid:{self.aid}评论未爬取到')

