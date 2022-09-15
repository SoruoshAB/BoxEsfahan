from django.db import models


class Slider(models.Model):
    type_choices = [(1, "Ad"), (2, "Video"), (3, "Song")]
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    image_link = models.TextField()
    link = models.TextField(blank=True, null=True)
    type = models.SmallIntegerField(choices=type_choices)

    def __str__(self):
        return str(self.id)
