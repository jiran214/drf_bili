from abc import ABC, abstractmethod
from apps.kol import models as Kol
from apps.note import models as Note


class Strategy(ABC):

    @abstractmethod
    def save(self, context,logger):
        pass

    @property
    def get_state(self):
        return self.state

class KolProcess(Strategy):

    @staticmethod
    def check_kol(mid):
        """检查外键"""
        try:
            ins = Kol.Info.objects.get(mid=str(mid))
            return ins
        except Exception as e:
            # print(e)
            return None

    @staticmethod
    def url_transform(image_url):
        before_url = 'https://i1.hdslb.com/bfs/face/'
        base_url = 'https://imgs-bz.feigua.cn/bfs/face/'
        url = image_url.split('/')[-1]
        return base_url + url

    def save(self, context,logger):
        context['face'] = self.url_transform(context['face'])
        mid = context['mid']
        kol = self.check_kol(mid)

        if kol is None:
            context.save()
            logger.info(f'创建Kol-mid:{mid}')
        else:
            kol.__dict__.update(**dict(context))
            kol.save()
            logger.info(f'更新Kol-mid:{mid}')


class NoteProcess(Strategy):

    @staticmethod
    def check_note(aid=None, cid=None):
        """检查外键"""
        try:
            if aid:
                ins = Note.Info.objects.get(aid=str(aid))
                return ins
            elif cid:
                ins = Note.Info.objects.get(cid=str(cid))
                return ins
        except Exception as e:
            # print(e)
            return None

    def save(self, context,logger):
        aid = context['aid']
        note = self.check_note(aid=aid)
        mid = context['mid']

        if note is None:
            kol = KolProcess.check_kol(mid)
            context['mid'] = kol

            context['pic'] = KolProcess.url_transform(context['pic'])
            context.save()
            logger.info(f'创建Note-mid:{mid}-aid:{aid}')
        else:
            filed_map = ('view_n', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like_n', 'update_time')
            for filed in filed_map:
                setattr(note, filed, context[filed])
            note.save()
            logger.info(f'更新Note-mid:{mid}-aid:{aid}')

class NoteStateProcess(Strategy):

    @staticmethod
    def get_item(context):
        filed_map = ('aid', 'view_n', 'danmaku', 'reply', 'reply', 'coin', 'share', 'like_n')
        item = {filed: context[filed] for filed in filed_map}
        item['aid'] = NoteProcess.check_note(aid=item['aid'])
        return item

    def save(self, context,logger):
        aid = context['aid']
        try:
            item = self.get_item(context)
            Note.Stat.objects.create(**item)
            logger.info(f'Note状态插入数据aid:{aid}')
        except Exception as e:
            logger.warn(f'Note状态可能已存在，不允许更新:{aid}-ERROT:{e}')


class KolStateProcess(Strategy):

    @staticmethod
    def get_item(context):
        filed_map = ('mid', 'following', 'follower', 'play_view', 'likes')
        item = {filed: context[filed] for filed in filed_map}
        item['mid'] = KolProcess.check_kol(mid=item['mid'])
        return item

    def save(self, context,logger):
        mid=context['mid']
        try:
            item = self.get_item(context)
            Kol.Stat.objects.create(**item)
            logger.info(f'Kol状态插入数据aid:{mid}')
        except Exception as e:
            print('KolStateProcess', e)
            logger.warn(f'Kol状态可能已存在，不允许更新:{mid}-ERROT:{e}')

class ContentProcess(Strategy):

    def check_oid(self , context,logger):
        msg=''
        try:
            if context['aid']:
                aid = NoteProcess.check_note(aid=context['aid'])
                context['aid'] =aid
                msg=str(context['aid'])
            elif context['cid']:
                cid =NoteProcess.check_note(cid=context['cid'])
                context['cid'] = cid
                msg=str(context['cid'])
            else:
                msg='没有找到aid和cid'
                return context
        except Exception as e:
            msg=f'没有找到外键{e}'
            return context

    def save(self, context,logger):
        oid = context['aid'] or context['cid']
        context=self.check_oid(context,logger)
        try:
            context.save()
            logger.info(f'oid:{oid}评论弹幕创建成功')
        except Exception as e:
            logger.warn(f'oid:{oid}可能重复主键{e}')

class HotwordProcess(Strategy):
    def save(self, context,logger):
        pass

class ItemContext():
    def __init__(self, spider, item):
        self.Stragety = []
        self.item = item
        self.logger=spider.logger

        if spider.name == 'get_kol':
            self.Stragety = [KolProcess,KolStateProcess]
        elif spider.name == 'get_note':
            self.Stragety = [NoteProcess,NoteStateProcess]
        elif spider.name == 'get_danmu_comment':
            self.Stragety = [ContentProcess,HotwordProcess]

    def context_interface(self):
        for s in self.Stragety:
            s().save(self.item,self.logger)
