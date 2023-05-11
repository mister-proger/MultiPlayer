import os
import threading
import pydub
import time
from pydub.playback import play as pydub_play
from typing import Optional


class Player:

    def __init__(self, path: str, chunk_size: int = 1024, delay: float = 0.1):

        self.path = path

        self.chunk_size = chunk_size

        self.delay = delay

        self.audio = pydub.AudioSegment.from_file(path)

        self.status = False

        self.flag = True

        self.pause_flag = False

        self.play_thread = threading.Thread(target=self.play)

    def play(self):

        if not self.status:

            self.status = True

            for chunk in self.audio[::self.chunk_size]:

                while self.pause_flag:

                    pass

                if not self.flag:

                    break

                pydub_play(chunk)

                time.sleep(self.delay)

            self.status = False

    def async_play(self):

        self.play_thread.start()

    def stop(self):

        self.flag = False

    def pause(self):

        self.pause_flag = True

    def resume(self):

        self.pause_flag = False

    def __del__(self):

        self.stop()
