from crawl.process import ItemContext
from crawl.settings import redis_conn

class MysqlPipeline:

    def process_item(self,item,spider):
        try:
            context = ItemContext(spider,item)
            context.context_interface()
            spider.logger.info(f'{spider.name}存储成功')
        except Exception as e:
            spider.logger.info(f'{spider.name}存储失败:',e)

        return item

class RedisPipeline:
    def process_item(self, item, spider):
        if spider.name == 'get_note':
            redis_conn.lpush('wait_cid', item['cid'])
            spider.logger.info(f'wait_cid更新')
            redis_conn.lpush('wait_aid', item['aid'])
            spider.logger.info(f'wait_cid更新')

        if spider.name == 'get_kol':
            redis_conn.lpush('wait_note_mid', item['mid'])
            spider.logger.info(f'wait_note_mid更新')

        return item


