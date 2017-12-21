from django.db import models

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=240)
    album_title=models.CharField(max_length=300)
    gener=models.CharField(max_length=200)
    album_logo=models.CharField(max_length=100)

    def __str__(self):
        return self.album_title + ' - ' + self.artist
class Song(models.Model):
    album_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=200)
    song_title=models.CharField(max_length=200)

    def __str__(self):
        return self.song_title
