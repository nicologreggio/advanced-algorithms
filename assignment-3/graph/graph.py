from collections import defaultdict
from functools import reduce
from glob import glob
#from random import random
from random import randint
from typing import NewType, Tuple, final, Set
from math import ceil, sqrt
import heapq as hq

GRAPH_FILE_EXTENSION = "txt"

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)
Cut=NewType("Cut", Tuple[Set[Vertex], Set[Vertex]])

# TODO: review all operations @nicolo
class Graph:
    def __init__(self, edges: "list[Edge]" = []):
        self.adj_list = defaultdict(lambda: defaultdict(list))

        # TODO: eventually adopt multiset (https://pypi.org/project/multiset/)
        self.edges = []

        self.weighted_degree = {}

        for s, t, w in edges:
            self.add_edge(s, t, w)

        # self.weighted_degree = {
        #     i: self.__calculate_weighted_degree(i) for i in self.get_vertices()
        # }

    def __calculate_weighted_degree(self, v: Vertex):
        """return the weighted degree of the vertex v"""
        return reduce(
            lambda a, b: a + sum(b), [x for x in self.adj_list[v].values()], 0
        )

    def get_vertices(self):
        """returns the list of vertices"""
        return self.adj_list.keys()

    def get_edges(self):
        """returns the list of edges"""
        return self.edges

    def get_adj_list_vertex(self, v: Vertex):
        """returns the adjaceny list of v"""
        return self.adj_list.get(v, None)

    def get_weighted_degree_list(self):
        """return the weighted degree list"""
        return self.weighted_degree

    def get_weight(self, s: Vertex, t: Vertex):
        """returns the weight of the edge (s,t), or None if such edge does not exist"""
        print(f"Weight from {s} to {t}: {self.adj_list[s][t]}")
        return sum(
            self.adj_list[s][t]
        )  # TODO: is it correct? I guess so, but we cannot discriminate edges when getting weights or looking up for them right? we just know they're there

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

        self.edges.append((s, t, w))
        self.edges.append((t, s, w))
        self.weighted_degree[s] = self.__calculate_weighted_degree(s)
        self.weighted_degree[t] = self.__calculate_weighted_degree(t)

    def remove_edge(self, s: Vertex, t: Vertex):
        """removes the edge from s to t and vice-versa"""
        ws = self.adj_list[s].get(t, None)

        if ws != None:
            self.adj_list[s].pop(t, None)
            self.adj_list[t].pop(s, None)

            for w in ws:
                self.edges.remove((s, t, w))
                self.edges.remove((t, s, w))

        self.weighted_degree[s] = self.__calculate_weighted_degree(s)
        self.weighted_degree[t] = self.__calculate_weighted_degree(t)

    def contract_edge(self, u: Vertex, v: Vertex):
        """Contracts the (u,v) edge"""
        self.remove_edge(u, v)

        for w in self.get_vertices():
            if w != u and w != v:
                self.add_edge(u, w, self.get_weight(w, v))
                self.remove_edge(w, v)

        del self.weighted_degree[v]
        del self.adj_list[v]

    def contract(self, k: int):
        """Contraction algorithms, unlike theory does not return anything because it side effects on instance graph"""
        for i in range(1, self.get_n() - k):
            u, v = edge_select(self)
            self.contract_edge(u, v)

    def recursive_contract(self) -> Tuple[Cut, int]:
        n = self.get_n()
        if n <= 6:
            #self.contract(2)
            self.contract(1)
            # return self.edges[0]#[2]  # they say "return weight of the only edge"...
            s,t,_=self.edges[0]
            w=self.get_weight(s,t)
            #return ((set([s]), set([t])), w)
            return w
        t = ceil(n / sqrt(2) + 1)

        ws = []
        for _ in range(1, 2):
            self.contract(t)
            ws.append(self.recursive_contract())

        #return ws[0] if ws[0][2] <= ws[1][2] else ws[1]
        return min(ws)  # boh

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())


# =====================================================================================

# FIND A PLACE FOR THIS STUF
def binary_search(g: Graph, C: list[int], r: int):
    start, next, end = 0, None, len(C) - 1
    found = False
    while start <= end and not found:
        next = (start + end) // 2
        if C[next - 1] <= r and r < C[next]:
            found = True
        elif C[next - 1] <= r:
            start = next + 1
        else:
            end = next

    return next if found else None


def random_select(g: Graph, C: list[int]) -> Edge:
    #r = random.randint(0, C[-1])
    r = randint(0, C[-1])
    e = binary_search(g, C, r)
    return e


def edge_select(g: Graph):
    D = g.get_weighted_degree_list()
    #C1 = [sum(D[:i]) for i in range(1, len(D) + 1)]
    C1 = [0 for _ in range(len(D))]
    C1[1] = D[1]
    for i in range(2, len(D)):
        C1[i] = C1[i - 1] + D[i]

    u = random_select(g, C1)

    C2 = [0 for _ in range(len(g.get_adj_list_vertex(u)))]
    for i in range(1, len(C2) - 1):
        C2[i] = C2[i - 1] + g.get_weight(u, i)

    v = random_select(g, C2)

    return (u, v)


# =========================================================


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
