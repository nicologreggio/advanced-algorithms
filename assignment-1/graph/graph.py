from glob import glob
from typing import NewType, Tuple 

Edge = NewType('Edge', Tuple[Tuple[int, int], int])
Vertex = NewType('Vertex', int)

GRAPH_FILE_EXTENSION = "txt"

class Graph:
    def __init__(self, n: int = 0, m: int = 0):
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

    def get_adj_list_vertex(self, v: int):
        return self.adj_list.get(v, None)

    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def add_edge(self, s: int, t: int, w: int):
        self.adj_list[s].update({t: w})
        self.adj_list[t].update({s: w})

        self.edges.add(((s, t), w))

    def remove_edge(self, s: int, t: int):
      if t in self.adj_list[s]:
        del self.adj_list[s][t]

      if s in self.adj_list[t]:
        del self.adj_list[t][s]

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

