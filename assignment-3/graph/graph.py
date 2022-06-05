from collections import defaultdict
from functools import reduce
from glob import glob

# from random import random
from random import randint
from typing import List, NewType, Tuple, final, Set
from math import ceil, sqrt
import heapq as hq

GRAPH_FILE_EXTENSION = "txt"

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)
Cut = NewType("Cut", Tuple[Set[Vertex], Set[Vertex]])

# TODO: review all operations @nicolo
class Graph:
    def __init__(self, edges: List[Edge] = []):
        self.adj_list = defaultdict(lambda: defaultdict(list))

        # TODO: eventually adopt multiset (https://pypi.org/project/multiset/)
        self.edges = set()

        self.weighted_degree = {}

        for s, t, w in edges:
            self.add_edge(s, t, w)

        # self.weighted_degree = {
        #     i: self.__calculate_weighted_degree(i) for i in self.get_vertices()
        # }

    def __calculate_weighted_degree(self, v: Vertex):
        """return the weighted degree of the vertex v"""

        """ def my_sum(a,b):
            return a + sum(b)
        return reduce(
            lambda a, b: my_sum(a,b), [x for x in self.adj_list[v].values()], 0
        ) """

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

    def get_nth_vertex(self, nth: int):
        """returns the nth vertex, starting from 0"""
        assert (
            nth < self.get_n()
        ), f"graph has {self.get_n()} vertices, so {nth} is out of bounds"
        it = iter(self.get_vertices())
        for _ in range(0, nth):
            next(it)
        return next(it)

    def get_adj_list_vertex(self, v: Vertex):
        """returns the adjaceny list of v"""
        return self.adj_list.get(v, None)

    def get_weighted_degree_list(self):
        """return the weighted degree list"""
        return self.weighted_degree

    def get_weight(self, s: Vertex, t: Vertex):
        """returns the weight of the edge (s,t), or None if such edge does not exist"""
        # TODO: is it correct? I guess so, but we cannot discriminate edges when getting weights or looking up for them right? we just know they're there
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
        # self.edges.append((t, s, w))
        self.weighted_degree[s] = self.__calculate_weighted_degree(s)
        self.weighted_degree[t] = self.__calculate_weighted_degree(t)

    def remove_edge(self, s: Vertex, t: Vertex):
        """removes the edge from s to t and vice-versa"""
        ws = self.adj_list[s].get(t, None)

        if ws != None:
            del self.adj_list[s][t]
            del self.adj_list[t][s]

            for w in ws:
                self.edges.discard((s, t, w))
                self.edges.discard((t, s, w))

        self.weighted_degree[s] = self.__calculate_weighted_degree(s)
        self.weighted_degree[t] = self.__calculate_weighted_degree(t)

    def contract_edge(self, u: Vertex, v: Vertex) -> "Graph":
        """Returns a new graph with the (u,v) edge contracted"""
        g = Graph(self.edges)
        g.remove_edge(u, v)

        for w in g.get_vertices():
            if w != u and w != v:
                weight = g.get_weight(w, v)
                if weight != 0:
                    g.add_edge(u, w, weight)
                    g.remove_edge(w, v)

        del g.weighted_degree[v]
        del g.adj_list[v]

        return g

    def contract(self, k: int) -> "Graph":
        """Returns a new graph contracted to k vertices"""
        g = self
        for i in range(1, self.get_n() + 1 - k):
            u, v = edge_select(self)
            g = g.contract_edge(u, v)
        return g

    def recursive_contract(self) -> Tuple[Cut, int]:
        g = self
        n = self.get_n()
        if n <= 6:
            g = self.contract(2)
            # self.contract(1) #shouldn't go like this, with the change in the cintract (n+1-k) should be fine now
            # return self.edges[0]#[2]  # they say "return weight of the only edge"...
            s, t, _ = g.edges[0]
            w = g.get_weight(s, t)
            # return ((set([s]), set([t])), w)
            return w
        t = ceil(n / sqrt(2) + 1)

        ws = []
        for _ in range(1, 2):
            g = self.contract(t)
            ws.append(g.recursive_contract())

        # return ws[0] if ws[0][2] <= ws[1][2] else ws[1]
        return min(ws)  # boh

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())


# =====================================================================================

# FIND A PLACE FOR THIS STUF
def binary_search(C: List[int], r: int):
    start, next, end = 0, None, len(C) - 1
    found = False
    print(f"list is {C} random val is {r}")
    while start <= end and not found:
        next = (start + end) // 2
        if C[next - 1] <= r and r < C[next]:
            found = True
        elif C[next - 1] <= r:
            start = next + 1
        else:
            end = next

    print(f"found this {next}")
    return next if found else None


def random_select(g: Graph, C: List[int]) -> Edge:
    # r = random.randint(0, C[-1])
    r = randint(0, C[-1])  # randint(a,b) gives n . a<=n<=b
    e = binary_search(C, r)
    # return e
    return g.get_nth_vertex(e)


def edge_select(g: Graph):
    D = g.get_weighted_degree_list()

    # C1 = [0 for _ in range(len(D))]
    # C1[1] = next(iter(D.values()))
    # for i in range(2, len(D)):
    #     C1[i] = C1[i - 1] + D[i]

    D_val = list(D.values())
    C1 = [sum(D_val[:i]) for i in range(1, len(D_val) + 1)]

    u = random_select(g, C1)
    print(f"nodes are: {g.get_vertices()}, bin search selected: {u}")

    # C2 = [0 for _ in range(len(g.get_adj_list_vertex(u)))]
    # for i in range(1, len(C2) - 1):
    #     C2[i] = C2[i - 1] + g.get_weight(u, i)

    W_val = list(g.get_adj_list_vertex(u).values())

    C2=[None] * len(W_val)
    C2[0]=sum(W_val[0])
    for i in range(1, len(W_val)): C2[i]=C2[i-1]+sum(W_val[i])

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
