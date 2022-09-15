from random import choices

from django.db import models


class Video(models.Model):
    type_choices = [(1, "ایرانی"), (2, "خارجی"), (3, "انیمیشن"), (4, "تبلیغ")]
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    image_link = models.TextField()
    link = models.TextField()
    type = models.SmallIntegerField(max_length=1, choices=type_choices)

    def __str__(self):
        return self.name
