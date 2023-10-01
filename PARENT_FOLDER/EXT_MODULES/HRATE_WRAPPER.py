import random
import threading
import time
import queue

import sys, os
# sys.path.append('..') # method 1
# sys.path.append(os.path.abspath('..')) # method 2
# sys.path.append(os.pardir) # method 3

import SHARED_MODULES.shared_data as shared_data

MAX_PULSE= 200
MIN_PULSE=50


class HrateInterface:
    is_running=False

    def __init__(self) -> None:
        pass

    def StartMeasure(self):
        HrateInterface.is_running = True
        self.measure_thread = threading.Thread(target=self._measure,args=(shared_data.data_queue,))
        self.measure_thread.start()

    def StopMeasure(self):
        HrateInterface.is_running = False

    def toggleMeasure(self):
        if HrateInterface.is_running :
            self.StopMeasure()
        else:
            self.StartMeasure()

    def _measure(self,data_queue,frequency=5):
        print("MEASURING STARTED")
        # global SHARED_VAL
        while HrateInterface.is_running:
            random_float = random.uniform(0.0, 1.0)
            hrate = MIN_PULSE + random_float*(MAX_PULSE-MIN_PULSE)
            
            data_queue.put(hrate)
            # print("HRATE saved: ",hrate)
            time.sleep(1/frequency)
            
        print("MEASURING STOPPED")





if __name__ == "__main__":
    hrate = HrateInterface()
    
    hrate.StartMeasure()
    time.sleep(2)
    hrate.StopMeasure()
    time.sleep(1)
    hrate.StartMeasure()
    time.sleep(2)
    hrate.StopMeasure()




