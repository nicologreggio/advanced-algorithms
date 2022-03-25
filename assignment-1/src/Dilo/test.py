from re import S
from heap import MyHeap
from random import seed, randint 
from time import perf_counter_ns    
import gc
import math 

alist = MyHeap([randint(1,100) for i in range(10)])
alist.build_min_heap()
print(alist)

alist.push(50)

print(alist)

alist.extract_min()

print(alist)