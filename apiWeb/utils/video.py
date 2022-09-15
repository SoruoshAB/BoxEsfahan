from apiWeb.models.video import Video


class UtilVideo:
    @staticmethod
    def get_video(video: Video):
        try:
            video_obj = {"id": int(video.id),
                         "image": str(video.image_link),
                         "link": str(video.link),
                         "is_ad": str(video.is_ad)}
            return video_obj
        except Exception as e:
            print("Error video :", str(e))
            return str(e)

    @staticmethod
    def get_latest_video():
        try:
            limit_video = 6
            latest_video_iranian = Video.objects.filter(type__in=[1]).order_by('-id')[:limit_video]
            latest_video_foreign = Video.objects.filter(type__in=[2]).order_by('-id')[:limit_video]
            latest_video_animation = Video.objects.filter(type__in=[3]).order_by('-id')[:limit_video]
            result_video_iranian = map(lambda video: UtilVideo.get_video(video),
                                       latest_video_iranian) if latest_video_iranian else []
            result_video_foreign = map(lambda video: UtilVideo.get_video(video),
                                       latest_video_foreign) if latest_video_foreign else []
            result_video_animation = map(lambda video: UtilVideo.get_video(video),
                                         latest_video_animation) if latest_video_animation else []
            result_video = {
                "iranian": result_video_iranian,
                "foreign": result_video_foreign,
                "animation": result_video_animation,
            }
            return result_video

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_video():
        try:
            all_video = Video.objects.order_by('-id')
            result_video = map(lambda video: UtilVideo.get_video(video), all_video) if all_video else []
            return result_video

        except Exception as e:
            return [str(e)]
