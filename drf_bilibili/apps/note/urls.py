# from  view import note
from rest_framework.routers import SimpleRouter
# from note.views import VideoInfoViewSet, NoteViewSet, NoteAddInfoViewSet, CommentViewSet, DetailInfoViewSet
from apps.note.views import NoteInfoViewSet, NoteDetailViewSet

router = SimpleRouter()
router.register(r'note', NoteInfoViewSet)
router.register(r'noteDetail', NoteDetailViewSet)
# router.register(r'addit',NoteAddInfoViewSet)
# router.register(r'detail',DetailInfoViewSet)
# router.register(r'note',NoteViewSet)
# router.register(r'comment',CommentViewSet)

urlpatterns = [
]
urlpatterns+=router.urls