from typing import Optional

from yandex_music import Client
import oshelp
import json
import infohelp


class YMClient:

    class Likes:

        def __init__(self, token: str, l_path: Optional[str] = None):

            self.client = Client(token).init()

            self.tracks = None

            if l_path:

                self.l_path = l_path if l_path.endswith("/") else l_path + "/"

            else:

                self.l_path = './data/likes/'

        def m_update(self) -> None:

            self.tracks = self.client.users_likes_tracks()

        def l_update(self, reboot: Optional[bool] = False, **param) -> None:

            def append_to_data(n_data):

                with open(self.l_path + 'data.json', 'r') as file:

                    f_data = json.load(file)

                if n_data in f_data:

                    print(f'Словарь "{n_data}" уже есть в файле {self.l_path}')

                    return None

                f_data.append(n_data)

                with open(self.l_path + 'data.json', 'w') as file:

                    json.dump(f_data, file)

                print(f'Словарь "{n_data}" успешно добавлен в файл {self.l_path}')

            if reboot:

                with open(self.l_path, 'w') as f:

                    json.dump([], f)

            oshelp.directory(self.l_path)

            for track in self.client.users_likes_tracks():

                track_info = infohelp.get(f'https://music.yandex.ru/album/{track.album_id}/track/{track.id}')

                if track.id in oshelp.files('./data/likes/', 'mp3'):

                    append_to_data({'id': {'track': track.id,
                                           'album': track.album_id},
                                    'name': {'track': track_info['title'] if not track_info['title'].endswith(' ') else track_info['title'][:-1],
                                             'album': track_info['album']},
                                    'icon': {'track': None,
                                             'album': None}})

                    continue

                oshelp.directory(self.l_path)

                self.client.tracks(track.id)[0].download(
                    f'{self.l_path}{track.id}.{param.get("codec", "mp3")}',
                    codec = param.get('codec', 'mp3'),
                    bitrate_in_kbps = param.get('kbps', 192)
                    )

                append_to_data({'id': {'track': track.id,
                                       'album': track.album_id},
                                'name': {'track': track_info['title'] if not track_info['title'].endswith(' ') else track_info['title'][:-1],
                                         'album': track_info['album']},
                                'icon': {'track': None,
                                         'album': None}})

        def l_d_update(self, priority: Optional[str] = 'files') -> None:

            if priority == 'files':

                values = oshelp.files(self.l_path, 'mp3')

                data = json.load(open(self.l_path + 'data.json', 'r'))

                for d in data[:]:  # Используем копию списка, чтобы избежать ошибок

                    if not d["id"]["track"] in values:

                        data.remove(d)

                with open(self.l_path + 'data.json', 'w') as file:

                    json.dump(data, file)

                return None

            elif priority == 'data':

                pass

            else:

                raise ValueError(f'Неизвестный тип исходных приоритетных данных: {priority}')


    def __init__(self, token: str):

        self.token = token

        self.client = Client(self.token).init()

        self.playlist_likes = self.Likes(token)

    def get_track(self, number: str, **param):

        return self.client.tracks(number)[0].download_bytes(
            codec = param.get('codec', 'mp3'),
            bitrate_in_kbps = param.get('kbps', 192)
        )

    def download_track(self, number: str, path: Optional[str] = './TEMP/', name: Optional[str] = None, **param):

        oshelp.directory(path)

        self.client.tracks(number)[0].download(
            f'{path if path.endswith("/") else path + "/"}{self.client.tracks(number)[0].title if name is None else name}.{param.get("codec", "mp3")}',
            codec = param.get('codec', 'mp3'),
            bitrate_in_kbps = param.get('kbps', 192)
        )

        return self.client.tracks(number)[0].title

    def get_user_playlists(self):

        return self.client.users_playlists_list()
