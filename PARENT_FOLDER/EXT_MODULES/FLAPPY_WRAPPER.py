# add "Flappy-bird-python" folder to path
import sys, os
# sys.path.append(os.path.abspath('Flappy-bird-python'))



# sys.path.append('..') # method 1
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append('Flappy_bird_python')

from EXT_MODULES.Flappy_bird_python import flappy

# chdir to current folder

# import flappy

def start():

    # flappy.start_game()
    flappy.lauch_game()

if __name__ == "__main__":
    start()