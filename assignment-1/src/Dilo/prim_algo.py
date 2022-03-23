from graph import Graph, Vertex
from graph import *
from heap import MyHeap
import heapq

# PRIM'S ALGORITHM - smart version with Heaps 

# version with my heaps
# this is not O(m*log(n))
def prim_algo(graph, s): 
    V = graph.get_vertices()
    E = graph.get_adlist()
    # can use float('inf') for the infinity 
    infty = float('inf')
    A = []
    S = list(map(lambda v: Vertex(v, infty), V))
    for v in S: 
        if v.name == s: 
            v.key = 0
    Q = MyHeap(S)
    Q.build_min_heap()
    while Q.list: 
        v = Q.extract_min()
        A.append(v)
        e = E.get(v.name)
        if e: 
            l = Q.list
            #print("l:", l)
            for u in e.keys(): 
                for i in range(len(l)):
                    if l[i].name == u and e.get(u) < l[i].key: 
                        l[i].key = e.get(u)
                        l[i].parent = v.name
                        #print("Q:", Q)
                        Q.min_heapify_up(i)   
                        #print("Q:", Q)      
        #heapq.heapify(Q)
    return A

# version with heapq library 
def prim_algo_hq(graph, s): 
    pass