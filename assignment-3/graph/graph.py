from collections import defaultdict
from glob import glob
from typing import NewType, Tuple
import heapq as hq

GRAPH_FILE_EXTENSION = "txt"

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)

# TODO: review all operations @nicolo
class Graph:
    def __init__(self, edges: "list[Edge]" = []):
        self.adj_list = defaultdict(lambda: defaultdict(list))
        self.edges = (
            []
        )  # TODO: eventually adopt multiset (https://pypi.org/project/multiset/)

        for s, t, w in edges:
            self.add_edge(s, t, w)

    def get_vertices(self):
        """returns the list of vertices"""
        return self.adj_list.keys()

    def get_edges(self):
        """returns the list of edges"""
        return self.edges

    def get_adj_list_vertex(self, v: Vertex):
        """returns the adjaceny list of v"""
        return self.adj_list.get(v, None)

    def get_weight(self, s: Vertex, t: Vertex):
        """returns the weight of the edge (s,t), or None if such edge does not exist"""
        print(f"Weight from {s} to {t}: {self.adj_list[s][t]}")
        return sum(self.adj_list[s][t])

    def get_n(self):
        """returns the number of nodes"""
        return len(self.adj_list)

    def get_m(self):
        """returns the number of edges"""
        return len(self.edges)

    def get_information(self, key):
        """returns the information associated to the given key"""
        return self.information.get(key, None)

    def add_edge(self, s: Vertex, t: Vertex, w):
        """adds an edge between the vertices s and t with weight w"""
        self.adj_list[s][t].append(w)
        self.adj_list[t][s].append(w)

        self.edges.append((s, t, w))
        self.edges.append((t, s, w))

    def remove_edge(self, s: Vertex, t: Vertex):
        """removes the edge from s to t and vice-versa"""
        ws = self.adj_list[s].get(t, None)

        if ws != None:
            self.adj_list[s].pop(t, None)
            self.adj_list[t].pop(s, None)

            for w in ws:
                self.edges.discard((s, t, w))
                self.edges.discard((t, s, w))

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())


# TODO: review from now on @diletta
def read_graph(f):
    lines = f.readlines()

    g = Graph()

    for l in lines[1:]:
        l = list(map(int, l.split()))
        g.add_edge(l[0], l[1], l[2])

    return g


def open_graph(file_path):
    with open(file_path, "r") as f:
        return read_graph(f)


def read_all(directory_path, size=None):
    files = read_sort_files(directory_path, size)
    return list(map(open_graph, files))


def read_sort_files(directory_path, size=None):
    files = sorted(glob(f"{directory_path}/*.{GRAPH_FILE_EXTENSION}"))
    return files if not size else files[:size]
