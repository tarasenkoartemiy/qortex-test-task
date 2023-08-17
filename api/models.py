from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=150)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["name", "executor"]

    def __str__(self):
        return f"ID : {self.id} | NAME : {self.name}"


class Album(models.Model):
    release_year = models.PositiveSmallIntegerField()
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track, through="AlbumTrack")

    def __str__(self):
        return str(self.id)


class AlbumTrack(models.Model):
    track = models.ForeignKey(Track, related_name="presence", on_delete=models.CASCADE)
    album = models.ForeignKey(
        Album, related_name="albumtracks", on_delete=models.CASCADE
    )
    serial_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ["track", "serial_number"]
