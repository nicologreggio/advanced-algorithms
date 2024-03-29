from graph import *
from heap import *
import heapq

# PRIM'S ALGORITHM - smart version with Heaps 
# version with my heaps
# THIS IS THE ONE!!
def prim_algo(graph, s): 
    E = graph.get_adlist()
    # can use float('inf') for the infinity 
    infty = float('inf')
    A = []
    Q = PriorityQueueVertex()
    for v in graph.get_vertices(): 
        vert = Vertex(v, infty if v!=s else 0, None)
        Q.push(vert)
    while Q.list: 
        v = Q.extract_min()
        A.append(v)
        e = E.get(v.name)
        for u in e.keys():
            n = Q.get_element(u)
            new_key = e[u]
            if n and new_key < n.key: 
                n.parent = v.name
                Q.decreaseKey(Q.get_index(u), new_key) 
    return A

'''
# this is not O(m*log(n))
def prim_algo_old(graph, s): 
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
                        l[i].parent = v.name
                        Q.decreaseKey(i, e.get(u))
                        #l[i].key = e.get(u)
                        #print("Q:", Q)
                        #Q.min_heapify_up(i)   
                        #print("Q:", Q)      
        #heapq.heapify(Q)
    return A

# version with heapq library 
def prim_algo_hq(graph, s): 
    V = graph.get_vertices()
    E = graph.get_adlist()
    # can use float('inf') for the infinity 
    infty = float('inf')
    A = []
    Q = list(map(lambda v: Vertex(v, infty), V))
    for v in Q: 
        if v.name == s: 
            v.key = 0
    heapq.heapify(Q)
    while Q: 
        v = heapq.heappop(Q)
        A.append(v)
        e = E.get(v.name)
        if e: 
            for u in e.keys(): 
                for i in Q:
                    if i.name == u and e.get(u) < i.key: 
                        Q.remove(i)
                        heapq.heappush(Q, Vertex(u, e.get(u), v.name))
    return A

# version for Graph_new - still not working 
def prim_algo_new(graph, s): 
    V = graph.get_vertices()
    E = graph.get_adlist()
    # E is now a list of lists 
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
        e = E[v.name-1][1:] # now this is a list of tuples 
        if e: 
            l = Q.list
            #print("l:", l)
            for u in e: # u is a tuple 
                for i in range(len(l)):
                    if l[i].name == u[0] and u[1] < l[i].key: 
                        l[i].parent = v.name
                        Q.decreaseKey(i, u[1])
                        #l[i].key = e.get(u)
                        #print("Q:", Q)
                        #Q.min_heapify_up(i)   
                        #print("Q:", Q)      
        #heapq.heapify(Q)
    return A
'''