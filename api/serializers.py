from rest_framework import serializers
from .models import Executor, Track, Album, AlbumTrack


def add_tracks_to_album(album, tracks_data):
    for track_data in tracks_data:
        track_pk = track_data.pop("track")
        album.tracks.add(track_pk, through_defaults=track_data)


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = "__all__"


class TrackPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumTrack
        fields = ["album", "serial_number"]


class TrackSerializer(serializers.ModelSerializer):
    presence = TrackPresenceSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = "__all__"


class AlbumTracksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumTrack
        fields = ["track", "serial_number"]


class AlbumSerializer(serializers.ModelSerializer):
    albumtracks = AlbumTracksSerializer(many=True)

    class Meta:
        model = Album
        exclude = ["tracks"]

    def validate_albumtracks(self, value):
        tracks = [track_data["track"] for track_data in value]
        if len(tracks) != len(set(tracks)):
            raise serializers.ValidationError("Album cannot contain duplicate tracks.")
        return value

    def create(self, validated_data):
        tracks_data = validated_data.pop("albumtracks")
        album = super().create(validated_data)
        add_tracks_to_album(album, tracks_data)
        return album

    def update(self, instance, validated_data):
        instance.tracks.clear()
        tracks_data = validated_data.pop("albumtracks")
        add_tracks_to_album(instance, tracks_data)
        return super().update(instance, validated_data)
