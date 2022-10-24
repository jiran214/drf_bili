from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from apps.note.filters import NoteFilter
from apps.note.ser import Info, Danmu, Comment, Danmu_hotwords, Comment_hotwords, \
    NoteInfoSer, NoteMessageSer, NoteDetailSer

from apps.note import tasks

class CustomSearchFilter(filters.SearchFilter):
    """
    定制化搜索
    """

    def get_search_fields(self, view, request):
        filed_search=('title', 'des', 'comment','tag')
        search_fileds=[]
        try:
            type=request.query_params.get('keyword_search_type')
            print(type)
            # if type is not None:
            #     type = int(type)
            # else:
            #     return response

            while type > 0:
                i = 1 # 位数
                if type & 1 == 1:
                    if i==2 or i==3:
                        #身份鉴权
                        if not request.user:
                            break
                    search_fileds.append(filed_search[i-1])
                type = type >>1
                i+=1

        except Exception as e:
            print(e)

        # print(request.user)
        # return super(CustomSearchFilter, self).get_search_fields(view, request)
        print(search_fileds)
        return search_fileds

class NotePagination(PageNumberPagination):
    """
    自定义分页类
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

    # ordering = ['bv']

# Create your views here.

class NoteInfoViewSet(mixins.ListModelMixin, GenericViewSet):
    # 认证权限
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [VipPermission]
    # throttle_classes = [AnonRateThrottle]

    queryset = Info.objects.order_by('-view_n')
    serializer_class = NoteInfoSer
    pagination_class = NotePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS

    filter_class = NoteFilter
    search_fields = ('title', 'des', 'aid', 'bvid')
    ordering_fields = ('view_n', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like_n')


class NoteDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    功能：评论分析、弹幕分析、人气表现

    retrieve:
    返回最新笔记的详情信息

    """
    queryset = Info.objects.all()
    serializer_class = NoteDetailSer


class NoteMessageViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Info.objects
    serializer_class = NoteMessageSer
