import time
import numpy as np
# ~ print("welcome to stopwatch") 


# ~ input()
# ~ st = time.time()
# ~ input()
# ~ ed = time.time() 

# ~ print( ed - st)


# ~ #d = a*t^2
# ~ d = 2 
# ~ a = 9.81
# ~ t = np.sqrt(d/a)  
# ~ print(t)


class stopwatch:
    def __init__(self):
        self.start_secs = 0 
        self.end_secs = 0 
        self.delta = 0 
        
    def timer(self):
        print( "Type enter to start" )
        input()
        self.start_secs = time.time()
        
        print( "type enter to end")
        input()
        self.end_secs = time.time()
        
        self.delta = self.end_secs - self.start_secs
        
    def sec_stopwatch(self):
        self.timer()
        print(" time was " + str(self.delta) + " secs")

    def min_stopwatch(self):
        self.timer()
        print(" time was " + str(self.delta/60.0) + " mins")


Secondstopper = stopwatch()
MinStopper = stopwatch()

Secondstopper.sec_stopwatch()
MinStopper.min_stopwatch()

