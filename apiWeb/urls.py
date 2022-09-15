from django.urls import path

from apiWeb.views.home import *
urlpatterns = [
    path('home/sliders', home_slider.as_view()),
    path('home/videos', home_video.as_view()),
    path('home/playlists', home_playlist.as_view()),
    path('home/podcasts', home_podcast.as_view()),
    path('home/books', home_book.as_view()),
]

