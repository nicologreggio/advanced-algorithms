# ANALYSIS 
from time import perf_counter_ns    
import gc
import math 
import random

def measure_run_time(graph, algo, num_calls): 
    # returns average runtime on a single graph
    gc.disable()
    start_time = perf_counter_ns()
    for i in range(num_calls):
        s = random.randint(1, graph.n_vert)
        algo(graph, s)
    end_time = perf_counter_ns()
    gc.enable()
    time = (end_time - start_time)/num_calls
    return time 
    
def filt(g, threshold = 2000): 
    return g.n_vert < threshold

def average(lst):
    return sum(lst) / len(lst)

def asymptotic_analysis(graph_list, algo, num_calls): # come parametro anche la funzione T(n, m) 
    # returns times on all graphs
    run_times = []
    c_estimates = []
    sizes = []
    print("V\tE\tT(ns)\tc_est")
    print(40*"-")
    #graphs = filter(filt, graph_list)
    #for g in graphs:
    for g in graph_list:
        t = measure_run_time(g, algo, num_calls)
        n, m = g.n_vert, g.n_edge
        sizes.append((n, m))
        c_est = round(t/(m*(math.log(n))), 3)
        c_estimates.append(c_est)
        run_times.append(t)
        print(n, m, t, c_est,sep="\t")
    print(40*"-") 
    print("average c_est =", average(c_estimates))
    return sizes, c_estimates, run_times

# generica funzione per il plot(c, T(n,m), [(n, m, t)]) 