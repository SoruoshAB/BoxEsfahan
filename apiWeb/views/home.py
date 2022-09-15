from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from apiWeb.utils.book import UtilBook
from apiWeb.utils.general import Util
from apiWeb.utils.playlist import UtilPlayList
from apiWeb.utils.podcast import UtilPodcast
from apiWeb.utils.slider import UtilSlider
from apiWeb.utils.video import UtilVideo


class home_slider(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilSlider.get_latest_slider())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_video(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilVideo.get_latest_video())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_playlist(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilPlayList.get_latest_playlist())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_podcast(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilPodcast.get_latest_podcast())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class home_book(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilBook.get_latest_book())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})
