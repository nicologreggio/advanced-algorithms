from graph import *
from heap import MyHeap
import heapq
from time import perf_counter_ns    
import math 
from analysis import * 
from prim_algo import * 
# elements in heap as (key, vertex, parent)

"""
#TEST                 


print(readAll())
"""
'''
'''
"""
f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
g = readGraph(f)

print(g.adlist)
print(prim_algo(g, 1))

print(g.adlist)
print(prim_algo(g, 1))
print(measure_run_time(g, prim_algo, 1))
print(measure_run_time(g, prim_algo, 10))
print(measure_run_time(g, prim_algo, 1000)) 
print(measure_run_time(g, prim_algo, 10000))
print(measure_run_time(g, prim_algo, 100000))
"""
'''
g = readGraph(f4)
print(g.adlist)
s = random.randint(1,g.n_vert)

start_time = perf_counter_ns()
A = prim_algo_hq(g, s)
end_time = perf_counter_ns()

time = (end_time - start_time)

print(A)
print(len(A))
print(time)
print(time/(g.n_edge*math.log(g.n_vert)))
'''


f1 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
f2 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_05_20.txt', 'r')
f3 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_21_200.txt', 'r')
f4 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_32_800.txt', 'r')
f5 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_43_4000.txt', 'r')
f6 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_53_20000.txt', 'r')

l = [f1, f2, f3, f4, f5, f6]
#l = [f1, f2, f3, f4, f5]

#A = readList_new(l)
A = readList(l)

asymptotic_analysis(A, prim_algo, 1)


'''
f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
g = readGraph_new(f)

print(g.adlist)
print(prim_algo_new(g, 1))
'''