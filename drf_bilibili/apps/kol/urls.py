from rest_framework.routers import SimpleRouter

from apps.kol.views import KolInfoViewSet, KolDetailViewSet

router = SimpleRouter()
router.register(r'kol', KolInfoViewSet)
router.register('kolDetail', KolDetailViewSet)

urlpatterns = [
]
urlpatterns += router.urls
