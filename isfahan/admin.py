from django.contrib import admin

from isfahan.models.event import Event
from isfahan.models.song import Song
from isfahan.models.video import Video

admin.site.register(Video)
admin.site.register(Song)
admin.site.register(Event)
