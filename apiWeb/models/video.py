from django.db import models


class Video(models.Model):
    type_choices = [(1, "Iranian"), (2, "Foreign"), (3, "Animation")]
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    image_link = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    type = models.SmallIntegerField(choices=type_choices)
    is_ad = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "-->" + self.get_type_display()
