# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class CrawlSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider): #yield
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# class MyRetryMiddleware(RetryMiddleware):
#
#     def process_response(self, request, response, spider):
#         # 在之前构造的request中可以加入meta信息dont_retry来决定是否重试
#         if request.meta.get('dont_retry', False):
#             return response
#         # 检查状态码是否在列表中，在的话就调用_retry方法进行重试
#         if response.status in self.retry_http_codes:
#             reason = response_status_message(response.status)
#             # 在此处进行自己的操作，如删除不可用代理，打日志等
#             spider.logger.warning(
#                 f"retry spider:{spider.name}|status:{response.status}|url:{request.url}"
#             )
#             record(spider.name,str(response.status))
#             time.sleep(2)
#             return self._retry(request, reason, spider) or response
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # 如果发生了Exception列表中的错误，进行重试
#         if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
#                 and not request.meta.get('dont_retry', False):
#             # 在此处进行自己的操作，如删除不可用代理，打日志等
#             spider.logger.warning(
#                 f"retry spider:{spider.name}|exception:{str(exception)}|url:{request.url}"
#             )
#             print(spider.name, str(exception))
#             return self._retry(request, exception, spider)

class CrawlDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        if response.status != 200:
            spider.logger.info(f'响应错误code:{response.status},url:{response.url}')
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        spider.logger.info(f'下载中间件异常:{exception}')
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
