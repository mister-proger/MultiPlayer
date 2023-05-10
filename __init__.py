from YMOperator import YMClient
from AOperator import Player

import time

#client = YMClient('')

# name = '23500213'

# client.download_track(name, name = name)

play = Player(f'./TEMP/23500213.mp3')

play.async_play()

del play
