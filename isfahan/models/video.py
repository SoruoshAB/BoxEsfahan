from django.db import models


class Video(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    image_link = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.name
