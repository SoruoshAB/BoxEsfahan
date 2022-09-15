from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models.book import Book
from .models.playList import PlayList
from .models.podcast import Podcast
from .models.slider import Slider
from .models.song import Song
from .models.video import Video

admin.site.site_header = "Isfahan Admin Panel"

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Slider)
admin.site.register(Video)
admin.site.register(Song)
admin.site.register(PlayList)
admin.site.register(Podcast)
admin.site.register(Book)
