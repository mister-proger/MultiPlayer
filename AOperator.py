import os
import wave
import threading
import subprocess
import pyaudio
from typing import Optional


class Player:

    class FileMeta:

        def __init__(self, path):

            with wave.open(path, 'rb') as file:

                self.channels = file.getnchannels()

                self.width = file.getsampwidth()

                self.rate = file.getframerate()

    def __init__(self, path: str):

        self.audio = pyaudio.PyAudio()

        self.path = f'./TEMP/{hex(hash(path[:path.rfind(".")]))[2:]}.wav'

        self.c_temp(path)

        self.data = self.FileMeta(self.path)

        self.stream = self.audio.open(format = self.audio.get_format_from_width(self.data.width),
                                      channels = self.data.channels,
                                      rate = self.data.rate,
                                      output = True)

        self.status = False

        self.flag = True

        self.play_thread = threading.Thread(target = self.play)

    def play(self):

        if not self.status:

            file = wave.open(self.path, 'rb')

            self.status = True

            data = file.readframes(1024)

            while self.flag and data:

                self.stream.write(data)

                data = file.readframes(1024)

            self.status = False

    def async_play(self):

        self.play_thread.start()

    def stop(self):

        self.flag = False

    def c_temp(self, path: Optional[str] = 'TEMP'):

        subprocess.call(['ffmpeg', '-i', path, '-ar', '44100', self.path],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                        )

    def __del__(self):

        self.stop()

        os.remove(self.path)
