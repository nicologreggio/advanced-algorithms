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
        # THIS HAS DUPLICATES! 
        E = []
        for i in self.get_vertices(): 
            for j in (self.adlist.get(i)).keys(): 
                if j > i: 
                    e = Edge((i, j), (self.adlist.get(i)).get(j))
                    E.append(e)
        return E
        # E = [({v, u}, w)] edge class 

    def get_kr_edges(self): 
        pass 

    def graph_infos(self): 
        print("n. of vertices: %d" %self.n_vert)
        print("n. of edges: %d" %self.n_edge)

# READ FROM ONE FILE
def readGraph(f): 
    lines = f.readlines()
    m = []
    info = list(map(int, lines[0].split()))
    n_vert, n_edge = info[0], info[1]
    for l in lines[1:]: 
        m.append(list(map(int, l.split())))
    h = {}
    for i in m: 
        if i[0] not in h: 
            h[i[0]] = {}
        if i[1] not in h: 
            h[i[1]] = {}
        h[i[0]][i[1]] = i[2]
        h[i[1]][i[0]] = i[2]
    g = Graph(h, n_vert, n_edge)
    return g

# READ ALL FILES 
import os
from tracemalloc import start

def open_graph(file_path):
	with open(file_path, 'r') as f:
		return readGraph(f)

def readAll(): 
    path = '/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1'
    os.chdir(path)
    A = []
    for file in os.listdir():
        file_path = f"{path}/{file}"
        g = open_graph(file_path)
        A.append(g)
    return A

def readList(l): 
    A = []
    for file in l:
        g = readGraph(file)
        A.append(g)
    return A

# VERTEX CLASS
class Vertex: 
    def __init__(self, name, key, parent = None): 
        self.name = name
        self.key = key
        self.parent = parent 

    def get_key(self): 
        return self.key

    def __lt__(self, other): 
        return self.key < other.key

    def __repr__(self):
        return "({0},{1},{2})".format(self.key, self.name, self.parent)

# EDGES CLASS 
class Edge: 
    def __init__(self, s, w): 
        self.s = s 
        self.w = w
    # set of edges + weight 

    def __lt__(self, other): 
        return self.w < other.w

    def __repr__(self): 
        return "({0}, {1})".format(self.s, self.w)

    def get_weight(self): 
        return self.w

    def get_vert_1(self): 
        return self.s[0]

    def get_vert_2(self): 
        return self.s[1]

    def __eq__(self, other):
        if self.get_weight() == other.get_weight() and ((self.get_vert_1() == other.get_vert_1() and self.get_vert_2() == other.get_vert_2()) or (self.get_vert_1() == other.get_vert_2() and self.get_vert_2() == other.get_vert_1())): 
            return True 
    # Error: unhashable type object 

'''
# Graph with adjacency list [[v1, (v2, w), (v3, w')], [v2, (v1, w), ...], ...]
class Graph_new: 
    def __init__ (self, adlist, n_vert, n_edge): 
        self.adlist = adlist 
        self.n_vert = n_vert
        self.n_edge = n_edge

    def __repr__(self): 
        return "(V: {0}, E: {1})".format(self.n_vert, self.n_edge)

    def get_vertices(self): 
        return list(range(1, self.n_vert+1))

    def get_adlist(self): 
        return self.adlist

    def graph_infos(self): 
        print("n. of vertices: %d" %self.n_vert)
        print("n. of edges: %d" %self.n_edge)

# READ FROM ONE FILE - graph new 
def readGraph_new(f): 
    lines = f.readlines()
    m = []
    info = list(map(int, lines[0].split()))
    n_vert, n_edge = info[0], info[1]
    for l in lines[1:]: 
        m.append(list(map(int, l.split())))
    h = [[i] for i in range(1, n_vert + 1)]
    for i in m: 
        h[i[0]-1].append((i[1], i[2]))
        h[i[1]-1].append((i[0], i[2]))
    g = Graph_new(h, n_vert, n_edge)
    return g

def readList_new(l): 
    A = []
    for file in l:
        g = readGraph_new(file)
        A.append(g)
    return A

'''