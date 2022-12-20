# from element import Element
import numpy as np
import sys
from gen import FunRand
import random

class Element:
    next_id = 0 
    
    def __init__(self,  delay= 1.0, delay_dev = 0.0, name = "-"):
        self.tnext = [0]
        self.id = Element.next_id 
        Element.next_id += 1
        self.delay_mean = delay
        self.delay_dev = delay_dev 
        self.distribution = ""
        self.quantity = 0
        self.tcurr = 0.0
        self.state = 0
        self.id = Element.next_id
        # self.proba = [1]
        self.next_element = None 
        self.name = name

        
    def get_delay(self):
        delay = self.get_delay_mean() 
        if ("exp" == (self.get_distribution())):
            delay = FunRand.Exp(self.get_delay_mean()) 
        
        elif("norm" == (self.get_distribution())):
            delay = FunRand.Norm(self.get_delay_mean(), self.get_delay_dev()) 
        
        elif ("unif" == (self.get_distribution())):
            delay = FunRand.Unif(self.get_delay_mean(),self.get_delay_dev()) 

        elif("" == (self.get_distribution())):
            delay = self.get_delay_mean() 

        return delay 
    
    def get_delay_dev(self):
        return self.delay_dev 
    
    def set_delay_dev(self, delay_dev: float):
        self.delay_dev = delay_dev 
    
    def get_distribution(self):
        return self.distribution 
    
    def set_distribution(self, distribution: str):
        self.distribution = distribution 
    
    def get_quantity(self) -> int:
        return self.quantity 
    
    def get_tcurr(self):
        return self.tcurr 
    
    def set_tcurr(self, tcurr: float):
        self.tcurr = tcurr 
    
    def get_state(self):
        return self.state 
    
    def set_state(self,  state: int):
        self.state = state 
    
    def get_next_element(self):
        return self.next_element 
    
    def set_next_element(self, next_element):
        self.next_element = next_element 
    
    def onStart(self):
        pass
    
    def onFinish(self):
        self.quantity += 1
    
    def get_tnext(self):
        return self.tnext 
    
    def set_tnext(self,  tnext: float):
        self.tnext = tnext 
    
    def get_delay_mean(self):
        return self.delay_mean 
    
    def set_delay_mean(self, delay_mean: float):
        self.delay_mean = delay_mean 
    
    def get_id(self):
        return self.id 
    
    def set_id(self, id: int):
        self.id = id 
    
    def print_result(self):
        print(self.get_name()+ " quantity = "+ str(self.quantity) )
    
    def print_info(self):
        print(self.get_name()+ " state= " +str(self.state)+"\
             How many requirements completed = "+ str(self.quantity)+" tnext= "+str(self.tnext) )
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def do_stats(self, delta: float):
        pass
  

    
