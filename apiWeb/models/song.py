from django.db import models

from apiWeb.models.playList import PlayList


class Song(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    playList = models.ForeignKey(PlayList, on_delete=models.Case)

    def __str__(self):
        return self.name
