import time
import queue

import SHARED_MODULES.shared_data as shared_data
import EXT_MODULES.dummy as dummy
from EXT_MODULES.HRATE_WRAPPER import HrateInterface


def main():
    shared_data.print_value()
    dummy.print_dummies()

    hrate_iface = HrateInterface()
    
    hrate_iface.StartMeasure()
    # time.sleep(3)
    read_hrate()
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