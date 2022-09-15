from isfahan.models.video import Video


class UtilVideo:
    @staticmethod
    def get_video(video: Video):
        try:
            video_obj = {"id": int(video.id),
                         "image": str(video.image_link),
                         "link": str(video.link)}
            return video_obj
        except Exception as e:
            print("Error video :", str(e))
            return str(e)

    @staticmethod
    def get_latest_video():
        try:
            latest_video = Video.objects.order_by('-id')[:6]
            result_video = map(lambda video: UtilVideo.get_video(video), latest_video) if latest_video else []
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
