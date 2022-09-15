from django.db import models


class Slider(models.Model):
    type_choices = [(1, "تبلیغ"), (2, "فیلم"), (3, "آهنگ")]
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    image_link = models.TextField()
    link = models.TextField(blank=True, null=True)
    is_ad = models.BooleanField(default=False)
    type = models.SmallIntegerField(max_length=1, choices=type_choices)

    def __str__(self):
        return self.id