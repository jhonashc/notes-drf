from rest_framework.routers import DefaultRouter
from apps.note.api.viewsets.note_viewset import NoteViewSet

router = DefaultRouter()

router.register(prefix='notes', viewset=NoteViewSet, basename='notes')

urlpatterns = router.urls