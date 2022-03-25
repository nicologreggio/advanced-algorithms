from re import S
from graph import *
from heap import *
from random import seed, randint 
from time import perf_counter_ns    
import gc
import math 

#A = [randint(1,100) for i in range(10)]
#V = [Vertex(a, a) for a in A]
V = []
alist = PriorityQueueVertex(V)
alist.build_min_heap()
print(alist, "\n")

alist.push(Vertex(50, 50))

print(alist, "\n")

alist.extract_min()

print(alist, "\n")