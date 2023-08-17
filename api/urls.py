from django.urls import path, include
from rest_framework import routers
from .views import ExecutorViewSet, TrackViewSet, AlbumViewSet

router = routers.SimpleRouter()
router.register(r"executors", ExecutorViewSet)
router.register(r"tracks", TrackViewSet)
router.register(r"albums", AlbumViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
