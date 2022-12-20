from element import Element
import sys
import numpy as np


class Process(Element):

    def __init__(self, delay: float, channels = 1, max_queue = sys.maxsize, distribution = "", name = None):
        super().__init__(delay) 
        self.queue = 0 
        self.name = name
        if self.name is None:
            self.name = "PROCESS"+str(self.id - 1) 
        self.mean_queue = 0.0 
        self.busy_time = 0.0
        #no failure: 0, yes failure : 1
        self.failure = 0
        self.proba = [1]
        self.max_queue = max_queue
        self.channels = channels
        self.distribution = distribution
        self.states = []
        for i in range(self.channels):
            self.states.append(0)
        self.tnext = []
        for i in range(self.channels):
            self.tnext.append(sys.float_info.max)

    def onStart(self):
        channels = []
        for i in range(self.channels):
            #available
            if self.states[i] == 0:
                channels.append(i)

        if channels:
            for i in channels:
                self.states[i] = 1
                self.tnext[i] = self.tcurr + super().get_delay()
                break
    
        else:
            if self.get_queue() < self.get_maxqueue():
                self.set_queue(self.get_queue() + 1) 
        
            else:
                self.failure+=1

    def define_proba_branch(self, proba = [1], nextElements = None):
        self.proba = proba
        self.next_element = nextElements

    def onFinish(self):
        tcurr_channels = []
        for i in range(self.channels):
            if self.tnext[i] == self.tcurr:
                tcurr_channels.append(i)
                
        for i in tcurr_channels:
            #quantity ++
            super().onFinish()

            self.tnext[i] = sys.float_info.max
            self.states[i] = 0

            if self.queue > 0:
                self.queue -= 1
                self.states[i] = 1
                self.tnext[i] = self.tcurr + self.get_delay()
                
            if self.next_element is not None:
                next_process = None
                if type(self.next_element) is Process or len(self.next_element) == 1:
                    #why choose one
                    next_process = np.random.choice(a=[self.next_element], p=[1])
                else:  
                    #type is list
                    next_process = np.random.choice(a=self.next_element, p=self.proba)

                next_process.onStart()
                
    def getNextEventTime():
        pass
    

    def get_failure(self):
        return self.failure 
    
    def get_queue(self):
        return self.queue 
    
    def set_queue(self, queue: int):
        self.queue = queue 
    
    def get_maxqueue(self)-> int:  
        return self.max_queue 
    
    def set_maxqueue(self, maxqueue:int):
        self.max_queue = maxqueue 
    
    def print_info(self):
        
        print(self.get_name() + " states= " + str(self.states) +
                " quantity = " + str(self.get_quantity()) +
                " tnext= " + str(self.tnext))
        print("failure = " + str(self.get_failure()) )
    

    def do_stats(self, delta: float):
        self.mean_queue = self.get_mean_queue() + self.queue * delta 
        for i in range(self.channels):
            self.busy_time = self.get_busy_time()+ delta * self.states[i]
        self.busy_time = self.busy_time / self.channels

    def get_busy_time(self):
        return self.busy_time     
    
    def get_mean_queue(self):
        return self.mean_queue 