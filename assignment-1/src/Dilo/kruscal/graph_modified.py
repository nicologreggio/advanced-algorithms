GRAPH_FILE_EXTENSION = "txt"
from glob import glob
from typing import NewType, Tuple 

Edge = NewType('Edge', Tuple[Tuple[int, int], int])
Vertex = NewType('Vertex', int)

class krEdge: 
    def __init__(self,s, t, w): 
        self.name = (s, t)
        self.weight = w
        self.label = None       # None, 0 for discovery, 1 for back 
        self.ancestor = None    # a node which is ancestor, maybe just 1 since need to find cycles

    def get_opposite(self, v): 
        if v == self.name[0]: 
            return self.name[1]
        elif v == self.name[1]: 
            return self.name[0]
        else: 
            return None 
    
    def change_label(self, l): 
        self.label = l

    def add_ancestor(self, a):
        self.ancestor = a

    def get_label(self): 
        return self.label()
    
    def __repr__(self): 
       #return "Edge({0}, {1})".format(self.name[0], self.name[1])
       return "({0}, {1})".format(self.name[0], self.name[1])

class Graph:
    def __init__(self, n: int, m: int):
        self.adj_list = {}
        self.n = n
        self.m = m
        self.edges = set()

        for i in range(1, n + 1):
            self.adj_list.update({i: {}})

    def get_vertices(self):
      return list(self.adj_list.keys())

    def get_edges(self):
      return self.edges

    def get_adj_list(self):
        return self.adj_list

    def get_adj_list_vertex(self, v: int):
        return self.adj_list.get(v, None)

    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def add_edge(self, s: int, t: int, w: int):
        self.adj_list[s].update({t: w})
        self.adj_list[t].update({s: w})

        self.edges.add(krEdge(s, t, w))

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.n, self.m)

def read_graph(f):
    lines = f.readlines()
    m = []
    info = list(map(int, lines[0].split()))

    n, m = info[0], info[1]
    g = Graph(n, m)

    for l in lines[1:]:
      l = list(map(int, l.split()))
      g.add_edge(l[0], l[1], l[2])

    return g


def open_graph(file_path):
  with open(file_path, 'r') as f:
    return read_graph(f)


def read_all(directory_path):
  files = read_sort_files(directory_path)
  return list(map(open_graph, files))


def read_sort_files(directory_path):
    return sorted(glob(f'{directory_path}/*.{GRAPH_FILE_EXTENSION}'))

