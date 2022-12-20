import csv
from process import Process
from create import Create
from testmodel import TestModel
from model import Model


def verify_with_params():
    distribution_type = ["exp", "unif", "norm"]
    create_delay = [0.5, 1.0, 1.5]
    process_delay = [0.8, 1.0, 1.5]
    queue_len = [5, 3]
    with open('results.csv','w') as file:
        fields = ["create_distribution", "create_delay","create_reqs served",
         "p1 distribution", "p1_delay", "p1_reqs served", "p1_queue_len","p1_failures", "p1_failure_prob", "p1_mean_queue", "p1_mean_business",
         "p2 distribution", "p2_delay", "p2_reqs served", "p2_queue_len", "p2_failures","p2_failure_prob", "p2_mean_queue", "p2_mean_business",
         "p3 distribution", "p3_delay", "p2_reqs served", "p3_queue_len", "p3_failures","p3_failure_prob", "p3_mean_queue", "p3_mean_business"]
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)

        for dt in distribution_type:
            for cd in create_delay:
                for pd in process_delay:
                    for ql in queue_len:
                        t = TestModel(dt, cd, pd, ql)
                        csvwriter.writerow(t.result)

def main():
    c =  Create(0.8) 
    p1 = Process(1.0, 1, 5, distribution='exp') 
    p2 = Process(1.0, 1, 5, distribution='exp') 
    p3 = Process(1.0, 1, 6, distribution='exp') 
    #print(f"id0 =  {c.getId()} id1= {p.getId()}") 
    c.set_next_element(p1) 
    p1.define_proba_branch(proba = [0.8, 0.2], nextElements=[p3, p2])


    l =  []
    l.append(c) 
    l.append(p1)
    l.append(p2)
    l.append(p3)
    model =  Model(l) 
    model.simulate(1000.0)





if __name__ == "__main__":
    main()