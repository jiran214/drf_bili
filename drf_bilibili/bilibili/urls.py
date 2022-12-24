
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include, re_path

from django.conf import settings
from apps.kol import urls as kol_urls
from apps.note import urls as note_urls
from apps.users import urls as user_urls
from apps.operation import urls as oper_urls

from rest_framework.documentation import include_docs_urls

from apps.test.view import TestView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(kol_urls)),
    path('', include(note_urls)),
    path('', include(user_urls)),
    path('', include(oper_urls)),
    re_path(r'docs/', include_docs_urls(title='接口文档')),
    path('', TestView.as_view()),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path(r'__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
