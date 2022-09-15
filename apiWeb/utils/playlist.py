from apiWeb.models.playList import PlayList


class UtilPlayList:
    @staticmethod
    def get_playlist(playlist: PlayList):
        try:
            songs = []
            if not playlist.is_ad:
                playlist_songs = playlist.song_set.values_list("link")
                for playlist_song in playlist_songs:
                    songs.append(playlist_song[0])
            playlist_obj = {"id": int(playlist.id),
                            "image_link": str(playlist.image_link),
                            "songs": songs,
                            "is_ad": str(playlist.is_ad)}
            return playlist_obj
        except Exception as e:
            print("Error playlist :", str(e))
            return str(e)

    @staticmethod
    def get_latest_playlist():
        try:
            latest_playlist = PlayList.objects.order_by('-id')[:6]
            result_playlist = map(lambda playlist: UtilPlayList.get_playlist(playlist),
                                  latest_playlist) if latest_playlist else []
            return result_playlist

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_playlist():
        try:
            all_playlist = PlayList.objects.order_by('-id')
            result_playlist = map(lambda playlist: UtilPlayList.get_playlist(playlist),
                                  all_playlist) if all_playlist else []
            return result_playlist

        except Exception as e:
            return [str(e)]
