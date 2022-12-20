from random import random 
import numpy as np

class FunRand:
    """
    @param timeMean mean value
    @return a random value according to an exponential
    distribution
    """

    def Exp(time_mean: float) -> float:
        a = 0
        while (a == 0):
            a = random()
        a = - time_mean * np.log(a)
        return a
    
    def Unif(time_min: float, time_max: float) -> float:
        a = 0
        while (a == 0):
            a = random()
        a = time_min + a * (time_max - time_min)
        return a


    def Norm(time_mean: float, time_deviation: float) -> float: 
        a = time_mean + time_deviation * np.random.normal()
        return a



