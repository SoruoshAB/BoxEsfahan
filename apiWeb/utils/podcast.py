from apiWeb.models.podcast import Podcast


class UtilPodcast:
    @staticmethod
    def get_podcast(podcast: Podcast):
        try:
            podcast_obj = {"id": int(podcast.id),
                           "name": str(podcast.name),
                           "channel": str(podcast.channel),
                           "image": str(podcast.image_link),
                           "link": str(podcast.link),
                           "is_ad": str(podcast.is_ad)}
            return podcast_obj
        except Exception as e:
            print("Error podcast :", str(e))
            return str(e)

    @staticmethod
    def get_latest_podcast():
        try:
            latest_podcast = Podcast.objects.order_by('-id')[:6]
            result_podcast = map(lambda podcast: UtilPodcast.get_podcast(podcast),
                                 latest_podcast) if latest_podcast else []
            return result_podcast

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_podcast():
        try:
            all_podcast = Podcast.objects.order_by('-id')
            result_podcast = map(lambda podcast: UtiPodcast.get_podcast(podcast), all_podcast) if all_podcast else []
            return result_podcast

        except Exception as e:
            return [str(e)]
