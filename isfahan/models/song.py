from django.db import models


class Song(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    image_link = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.name
