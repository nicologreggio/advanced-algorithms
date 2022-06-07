from collections import defaultdict
from functools import reduce
from glob import glob

# from random import random
from typing import List, NewType, Tuple, Set

GRAPH_FILE_EXTENSION = "txt"

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)
Cut = NewType("Cut", Tuple[Set[Vertex], Set[Vertex]])

# TODO: review all operations @nicolo
class Graph:
    def __init__(self, edges: List[Edge] = []):
        self.adj_list = defaultdict(lambda: defaultdict(list))
        self.edges = set()
        self.weighted_degree = defaultdict(int)

        for s, t, w in edges:
            self.add_edge(s, t, w)

    def __calculate_weighted_degree(self, v: Vertex):
        """return the weighted degree of the vertex v"""

        acc = 0
        for x in self.adj_list[v].values():
            acc += sum(x)
        return acc

    def get_vertices(self):
        """returns the list of vertices"""
        return self.adj_list.keys()

    def get_edges(self):
        """returns the list of edges"""
        return self.edges

    def get_adj_list_vertex(self, v: Vertex):
        """returns the adjaceny list of v"""
        return self.adj_list.get(v, None)

    def remove_vertex(self, v: Vertex):
        del self.weighted_degree[v]
        del self.adj_list[v]

    def get_weighted_degree_list(self):
        """return the weighted degree list"""
        return self.weighted_degree

    def get_weight(self, s: Vertex, t: Vertex):
        """returns the weight of the edge (s,t), or None if such edge does not exist"""
        return sum(self.adj_list[s].get(t, []))

    def get_n(self):
        """returns the number of nodes"""
        return len(self.adj_list)

    def get_m(self):
        """returns the number of edges"""
        return len(self.edges)

    def add_edge(self, s: Vertex, t: Vertex, w):
        """adds an edge between the vertices s and t with weight w"""
        self.adj_list[s][t].append(w)
        self.adj_list[t][s].append(w)

        self.edges.add((s, t, w))

        self.weighted_degree[s] += w  # self.__calculate_weighted_degree(s)
        self.weighted_degree[t] += w  # self.__calculate_weighted_degree(t)

    def remove_edge(self, s: Vertex, t: Vertex):
        """removes the edge from s to t and vice-versa"""
        ws = self.adj_list[s].get(t, None)

        if ws != None:
            del self.adj_list[s][t]
            del self.adj_list[t][s]

            edges_weight = 0
            for w in ws:
                edges_weight += w
                self.edges.discard((s, t, w))
                self.edges.discard((t, s, w))

            self.weighted_degree[s] -= edges_weight
            self.weighted_degree[t] -= edges_weight

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())


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
