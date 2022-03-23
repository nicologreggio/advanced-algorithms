from graph import Graph, Vertex
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

f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_16_80.txt', 'r')
g = readGraph(f)

print(g.adlist)

start_time = perf_counter_ns()
A = prim_algo(g, 1)
end_time = perf_counter_ns()

time = (end_time - start_time)

print(A)
print(len(A))
print(time)
print(time/(g.n_edge*math.log(g.n_vert)))