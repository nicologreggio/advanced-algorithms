from re import S
from heap import MyHeap
from random import seed, randint 
from time import perf_counter_ns    
import gc
import math 

def average(lst):
    return sum(lst) / len(lst)

def measure_run_time(list_size, num_calls, num_instances):
  sum_times = 0.0
  for i in range(num_instances):
    alist = MyHeap([randint(0,10000) for i in range(list_size)])
    gc.disable()
    alist.build_min_heap()    
    start_time = perf_counter_ns()
    for i in range(num_calls): 
        #s = randint(0, alist.size)
        #alist.list[s] = randint(0,10000)
        #alist.min_heapify_up(s)
        alist.extract_min()
    end_time = perf_counter_ns()
    gc.enable()
    sum_times += (end_time - start_time)/num_calls
  avg_time = int(round(sum_times/num_instances))
  # return average time in nanoseconds
  return avg_time

list_sizes = [10*(2**i) for i in range(12)]
num_calls = 1
num_instances = 4
run_times = [measure_run_time(size, num_calls, num_instances) for size in list_sizes]

#ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(list_sizes)-1)]
c_estimates = [round(run_times[i]/math.log(list_sizes[i]),3) for i in range(len(list_sizes))]
print("num_calls: %d, num_instances: %d", (num_calls, num_instances))
print("Size\tTime(ns)\tCostant\t")
print(50*"-")
for i in range(len(list_sizes)):
  print(list_sizes[i], run_times[i], '', c_estimates[i], '', sep="\t")
print(50*"-")
avg = average(c_estimates)
print("average c:", avg)

# build_min_heap     O(n)       avg_c = 300 circa ok 
# extract_min        O(log n)   avg_c = 1240 circa ok   -> non si può testare su più chiamate però 
# min_heapify        O(log n)   avg_c = 470 circa ok 