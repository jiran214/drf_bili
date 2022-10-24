from rest_framework.routers import SimpleRouter

from apps.kol.views import KolInfoViewSet, KolDetailViewSet, kolMessageViewSet

router = SimpleRouter()
router.register('kol', KolInfoViewSet)
router.register('kolDetail', KolDetailViewSet)
router.register('kolMessage', kolMessageViewSet)

urlpatterns = [
]
urlpatterns += router.urls
