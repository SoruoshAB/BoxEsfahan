from django.urls import path

from isfahan.views import *

urlpatterns = [
    path('isf/videos', isf_video.as_view()),
    path('isf/songs', isf_song.as_view()),
    path('isf/events', isf_event.as_view()),
]
