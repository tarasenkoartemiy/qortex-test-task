from rest_framework.viewsets import ModelViewSet
from .models import Executor, Track, Album
from .serializers import ExecutorSerializer, TrackSerializer, AlbumSerializer


class ExecutorViewSet(ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_destroy(self, instance):
        instance.tracks.clear()
        return super().perform_destroy(instance)
