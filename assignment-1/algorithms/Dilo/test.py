from re import S
from graph import *
from heap import *
from random import seed, randint 
from time import perf_counter_ns    
import gc
import math 

#A = [randint(1,100) for i in range(10)]
A = [0, 48, 21, 30, 47, 11, 12, 15, 18, 66]
#V = [Vertex(a, a) for a in A]
alist = PriorityQueueVertex()
for a in A: 
    alist.push(Vertex(a, a))
#alist.build_min_heap()
print(alist, "\n")

alist.push(Vertex(50, 50))
print(alist.get_index(50))
print(alist, "\n")

print(alist.list[10])

alist.extract_min()
print(alist.get_index(21))
print(alist.get_element(21))



print(alist, "\n")