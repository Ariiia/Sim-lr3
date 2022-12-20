import sys
from process import Process
from element import Element
import numpy as np


class Model:

    def __init__(self, elements):
        self.l = elements 
        self.tnext = 0.0 
        self.next_event_id = 0 
        self.tcurr = 0.0

    def simulate(self, time: float):
        while (self.tcurr < time):
            
            self.tnext = sys.float_info.max

            for e in self.l:
                #find closest 
                next_event_time = np.min(e.tnext)

                if (next_event_time < self.tnext):
                    self.tnext = next_event_time
                    self.next_event_id = e.get_id() 
            #print("\nIt's time for event in " + str(self.l[self.NextEventId].getName()) +", time = " + str(self.tnext)+ "quantity:"+ str(self.l[self.NextEventId].quantity))

            e_duration = self.tnext - self.tcurr
            self.tcurr = self.tnext 

            for e in self.l:
                e.set_tcurr(self.tcurr) 
                e.do_stats(e_duration)
            
            if len(self.l) > self.next_event_id:
                self.l[self.next_event_id].onFinish() 

            for e in self.l:
                if self.tcurr in e.tnext:
                    e.onFinish() 


            self.print_info() 
        #renew simulacr
        Element.next_id = 0
        self.print_result() 

        return self.extract_stats() 
    
    def print_info(self):
        for e in self.l:
            e.print_info() 
    
    def extract_stats(self):
        results_process = []
        results_create = []
        for e in self.l:
            if type(e) is Process:
                p = e
                results_process+=[p.get_distribution(), p.get_delay_mean(), p.get_quantity(), p.get_maxqueue(), 
                p.get_failure(), p.get_failure() / p.get_quantity(), p.get_mean_queue()/self.tcurr, p.get_busy_time()/self.tcurr]
            else:
                results_create = [e.get_distribution(), e.get_delay_mean(), e.get_quantity()]

        results_create+=results_process
        

        return results_create

    def print_result(self):
        print("\n-------------RESULTS-------------") 
        for e in self.l:
            e.print_result() 
            if type(e) is Process:
                p = e
                print(f"mean length of queue = {p.get_mean_queue() / self.tcurr} \nfailure probability = \
                {p.get_failure() / p.get_quantity()}) \nfailures: {p.get_failure()}\
                \n mean busy time = {p.get_busy_time() / self.tcurr}")

