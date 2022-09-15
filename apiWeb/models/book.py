from django.db import models


class Book(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    Publishers = models.CharField(max_length=20)
    image_link = models.TextField()
    link = models.TextField()
    is_ad = models.BooleanField(default=False)

    def __str__(self):
        return self.name
