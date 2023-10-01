import time
import queue
import os,sys

import SHARED_MODULES.shared_data as shared_data
import EXT_MODULES.dummy as dummy
from EXT_MODULES.HRATE_WRAPPER import HrateInterface
import EXT_MODULES.FLAPPY_WRAPPER as flappy_wrapper

def main():
    shared_data.print_value()
    dummy.print_dummies()

    # os.chdir("PARENT_FOLDER\\EXT_MODULES\\Flappy_bird_python")
    flappy_wrapper.start()

    hrate_iface = HrateInterface()
    
    hrate_iface.StartMeasure()
    # time.sleep(3)
    read_hrate(duration=3,frequency=5)
    hrate_iface.StopMeasure()

def read_hrate(duration=5,frequency=1):
    for _ in range(duration*frequency):
        try:
            data_from_thread = shared_data.data_queue.get(block=False)  # Non-blocking get
            print("Received:", data_from_thread)
        except queue.Empty:
            print("No data in the queue.")
        time.sleep(1/frequency)  # Sleep for a while to avoid busy-waiting




if __name__ == "__main__":
    main()