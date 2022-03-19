# GRAPH CLASS 
class Graph: 
    def __init__ (self, adlist, n_vert, n_edge): 
        self.adlist = adlist 
        self.n_vert = n_vert
        self.n_edge = n_edge

    def __repr__(self): 
        return "(V: {0}, E: {1})".format(self.n_vert, self.n_edge)

    def get_vertices(self): 
        return list(self.adlist.keys())

    def get_adlist(self): 
        return self.adlist

    def get_edges(self): 
        # list of edges: cannot set E = set() because of "TypeError: unhashable type: 'set'"
        # should anyway not have duplicates for how it is written. 
        E = []
        for i in self.get_vertices(): 
            for j in (self.adlist.get(i)).keys(): 
                E.append(({i, j}, (self.adlist.get(i)).get(j)))
        return E
        # E = [({v, u}, w)]

    def graph_infos(self): 
        print("n. of vertices: %d" %self.n_vert)
        print("n. of edges: %d" %self.n_edge)

# READ FROM ONE FILE
def readGraph(f): 
    # adjacency list is "directed" in the way the graph is written in the document
    # TO DO: fix this 
    lines = f.readlines()
    m = []
    info = list(map(int, lines[0].split()))
    n_vert, n_edge = info[0], info[1]
    for l in lines[1:]: 
        m.append(list(map(int, l.split())))
    h = {}
    for i in m: 
        if i[0] not in h: 
            h[i[0]] = {i[1]:i[2]}
        else: 
            h[i[0]].update({i[1]:i[2]})
    g = Graph(h, n_vert, n_edge)
    return g

# READ ALL FILES 
import os

def open_graph(file_path):
	with open(file_path, 'r') as f:
		return readGraph(f)

def readAll(): 
    path = "/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1"
    os.chdir(path)
    A = []
    for file in os.listdir():
        file_path = f"{path}/{file}"
        g = open_graph(file_path)
        A.append(g)
    return A

# PRIM'S ALGORITHM - smart version with Heaps 

# use predefined heaps or heapq library?
# how to store information in the heapq? name of vertex, priority (which is what should be used to order the heap), parent

import heapq

# elements in heap as (key, vertex, parent)
# can use float('inf') for the infinity 

class Vertex: 
    def __init__(self, name, key, parent = None): 
        self.name = name
        self.key = key
        self.parent = parent 

    def __lt__(self, other): 
        return self.key < other.key

    def __repr__(self):
        return "({0},{1},{2})".format(self.key, self.name, self.parent)


def prim_algo(graph, s): 
    V = graph.get_vertices()
    E = graph.get_adlist()
    infty = float('inf')
    A = []
    Q = list(map(lambda v: Vertex(v, infty), V))
    for v in Q: 
        if v.name == s: 
            v.key = 0
    heapq.heapify(Q)
    while bool(Q): 
        v = heapq.heappop(Q)
        A.append(v)
        e = E.get(v.name)
        if e: 
            for u in e.keys(): 
                for l in Q:
                    if l.name == u and e.get(u) < l.key: 
                        l.parent = v.name 
                        l.key = e.get(u) 
        heapq.heapify(Q)
    return A
    
"""
#TEST 

print(readAll())

f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_20_100.txt', 'r')

g = readGraph(f)

#print(g.adlist)
print(prim_algo(g, 1))

"""

