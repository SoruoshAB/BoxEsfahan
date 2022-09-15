from isfahan.models.song import Song


class UtilSong:
    @staticmethod
    def get_song(song: Song):
        try:
            song_obj = {"id": int(song.id),
                        "name": str(song.name),
                        "image": str(song.image_link),
                        "link": str(song.link)}
            return song_obj
        except Exception as e:
            print("Error song :", str(e))
            return str(e)

    @staticmethod
    def get_latest_song():
        try:
            latest_song = Song.objects.order_by('-id')[:6]
            result_song = map(lambda song: UtilSong.get_song(song), latest_song) if latest_song else []
            return result_song

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_song():
        try:
            all_song = Song.objects.order_by('-id')
            result_song = map(lambda song: UtilSong.get_song(song), all_song) if all_song else []
            return result_song

        except Exception as e:
            return [str(e)]
