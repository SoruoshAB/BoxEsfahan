from django.db import models


class Podcast(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    channel = models.CharField(max_length=20, blank=True, null=True)
    image_link = models.TextField()
    link = models.TextField(blank=True, null=True)
    is_ad = models.BooleanField(default=False)

    def __str__(self):
        return self.name
