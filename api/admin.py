from django.contrib import admin
from .models import Executor, Album, Track, AlbumTrack


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ["name"]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id", "release_year", "executor"]
    ordering = ["release_year"]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "executor"]
    ordering = ["name"]


@admin.register(AlbumTrack)
class AlbumTrackAdmin(admin.ModelAdmin):
    list_display = ["id", "track", "album", "serial_number"]
    ordering = ["album"]
