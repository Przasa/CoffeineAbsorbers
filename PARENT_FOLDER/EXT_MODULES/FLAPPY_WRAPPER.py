import sys, os
import threading

from EXT_MODULES.Flappy_bird_python import flappy

# sys.path.append('..') # method 1
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append('Flappy_bird_python')


class FlappyInterface:

    def __init__(self) -> None:
        pass
# chdir to current folder

# import flappy

    def StartFlappy(self):
        flappy_thread = threading.Thread(target=flappy.lauch_game)
        flappy_thread.start()


if __name__ == "__main__":
    flappy_iface = FlappyInterface()
    flappy_iface.StartFlappy()
