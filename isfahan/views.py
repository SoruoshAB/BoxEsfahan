from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from isfahan.utils.event import UtilEvent
from isfahan.utils.general import Util
from isfahan.utils.song import UtilSong
from isfahan.utils.video import UtilVideo


class isf_video(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilVideo.get_latest_video())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class isf_song(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilSong.get_latest_song())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})


class isf_event(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request: HttpRequest):
        try:
            return Util.response_generator("ok", 200, UtilEvent.get_latest_event())
        except Exception as e:
            return Util.response_generator("internal server error", 500, {str(e)})
