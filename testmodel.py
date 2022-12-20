from create import Create
from process import Process
from model import Model


class TestModel:
    def __init__(self, distribution_type, create_delay, process_delay, queue_len):
        c =  Create(create_delay) 
        p1 = Process(process_delay) 
        p2 = Process(process_delay)
        p3 = Process(process_delay)
        #print(f"id0 =  {c.getId()} id1= {p.getId()}") 
        c.set_next_element(p1) 
        p1.set_next_element(p2)
        p2.set_next_element(p3)

        p1.set_maxqueue(queue_len) 
        p2.set_maxqueue(queue_len) 
        p3.set_maxqueue(queue_len)

        c.set_name("CREATOR") 
        p1.set_name("PROCESSOR1") 
        p2.set_name("PROCESSOR2") 
        p3.set_name("PROCESSOR3") 

        c.set_distribution(distribution_type) 
        p1.set_distribution(distribution_type) 
        p2.set_distribution(distribution_type)
        p3.set_distribution(distribution_type)

        l =  []
        l.append(c) 
        l.append(p1)
        l.append(p2)
        l.append(p3) 
        model =  Model(l) 
        self.result = model.simulate(1000.0)
