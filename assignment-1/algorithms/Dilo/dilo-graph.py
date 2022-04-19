from graph import *
from heap import *
import heapq
from time import perf_counter_ns    
import math 
from analysis import * 
from prim_algo import * 
# elements in heap as (key, vertex, parent)


#TEST                 

A = readAll()

asymptotic_analysis(A, prim_algo, 10)

"""
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

'''
f1 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
f2 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_05_20.txt', 'r')
f3 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_21_200.txt', 'r')
f4 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_32_800.txt', 'r')
f5 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_43_4000.txt', 'r')
f6 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_53_20000.txt', 'r')
f7 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_63_80000.txt', 'r')
f8 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_68_100000.txt', 'r')

#l = [f1, f2]
l = [f1, f2, f3, f4, f5, f6,f7,f8]
#l = [f1, f2, f3, f4, f5]

#A = readList_new(l)
#A = readList(l)
'''

'''
f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_03_10.txt', 'r')
g = readGraph(f)

print(g.adlist, "\n")
print(prim_algo(g, 1))
'''
'''
f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
g = readGraph_new(f)

print(g.adlist)
print(prim_algo_new(g, 1))

g = readGraph(f1)
print(g.adlist)

E = g.get_adlist()
infty = float('inf')
A = []
Q = PriorityQueueVertex()
for v in g.get_vertices(): 
    vert = Vertex(v, infty if v!=1 else 0, None)
    Q.push(vert)
print("Q:", Q, "\n")
while Q.list: 
    v = Q.extract_min()
    print("v:", v)
    A.append(v)
    print("A:", A)
    e = E.get(v.name)
    print("e:", e)
    #print("e.keys:", e.keys())
    for u in e.keys():
        n = Q.get_element(u)
        print("n:", n, "\n")
        new_key = e[u]
        if n and new_key < n.key: 
            n.parent = v.name
            Q.decreaseKey(Q.get_index(u), new_key) 
            print("n update:", n, "\n")
'''