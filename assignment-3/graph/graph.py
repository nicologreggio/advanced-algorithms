from collections import defaultdict
from functools import reduce
from glob import glob

# from random import random
from random import randint, randrange
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

    """
    Try to build it not as a graph function
    def get_nth_vertex(self, nth: int):
        # now should work with e-1
        #returns the nth vertex, starting from 0
        assert (
            #nth < self.get_n()
            nth < self.get_n()
        ), f"graph has {self.get_n()} vertices, so {nth} is out of bounds"
        it = iter(self.get_vertices())
        for _ in range(0, nth):
            next(it)
        return next(it)"""

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
        n = self.get_n()
        #print("number of vertices:", n)
        #for _ in range(1, self.get_n() + 1 - k): this keeps on updating self.get_n()! 
        for _ in range(1, n + 1 - k): 
            #u, v = edge_select(self)
            u, v = edge_select(g) # should use the updated graph! 
            g = g.contract_edge(u, v)
            #print("vertices after contraction:", g.get_n())
        return g

    def recursive_contract(self) -> Tuple[Cut, int]:
        g = self
        n = self.get_n()
        if n <= 6:
            g = self.contract(2)
            #s, t, _ = g.edges[0]
            s, t = g.get_vertices()
            #print(s)
            #print(t)
            w = g.get_weight(s, t)
            #print(w)
            return w
        t = ceil(n / sqrt(2) + 1)

        ws = []
        for _ in range(1, 2):
            g = self.contract(t)
            ws.append(g.recursive_contract())

        return min(ws)  

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())

def get_nth_vertex(d, nth: int): # d is a list of keys
        # now should work with e-1
        """returns the nth vertex, starting from 0"""
        assert (
            #nth < self.get_n()
            nth < len(d)
        ), f"dictionary has {len(d)} vertices, so {nth} is out of bounds"
        it = iter(d)
        for _ in range(0, nth):
            next(it)
        return next(it)

# =====================================================================================

# FIND A PLACE FOR THIS STUF

def binary_search(C: List[int], r: int): # returns an int if found, None if not found. 
    # NB: in our case should never return None, because we're choosing r exactly in the correct range. 
    #start, next, end = 0, None, len(C) - 1
    start, next, end = 0, None, len(C) 
    found = False
    #print(f"list is {C} random val is {r}")
    while start < end and not found:
        next = (start + end) // 2
        if C[next - 1] <= r and r < C[next]:
            found = True
        elif C[next - 1] <= r:
            start = next + 1
        else:
            end = next
    """if found: 
        print(f"found this {next}")
    else: 
        print("not found")"""
    return next if found else None


#def random_select(g: Graph, C: List[int]) -> Vertex: #(g: Graph, C: List[int]) -> Edge:
def random_select(C: List[int], d) -> Vertex: # d should be a list of keys 
    # r = random.randint(0, C[-1])
    #r = randint(0, C[-1])  # randint(a,b) gives n . a<=n<=b
    r = randrange(0, C[-1]) # I don't want to have the last one included
    e = binary_search(C, r)
    # return e
    #return g.get_nth_vertex(e-1) # because of the update in the indeces
    return get_nth_vertex(d, e-1)


def edge_select(g: Graph):
    D = g.get_weighted_degree_list()

    D_val = list(D.values())
    #C1 = [sum(D_val[:i]) for i in range(1, len(D_val) + 1)]
    C1 = [0] + [sum(D_val[:i]) for i in range(1, len(D_val) + 1)] 
    # should start from 0, in order to be able to select also the first vertex. 
    #print(C1)

    #u = random_select(g, C1)
    u = random_select(C1, g.get_vertices())
    #print(f"nodes are: {g.get_vertices()}, bin search selected: {u}")

    W_val = list(g.get_adj_list_vertex(u).values())

    C2=[None] * (len(W_val) + 1)
    #C2[0]=sum(W_val[0])
    C2[0] = 0
    # also this should start from 0, in order to be able to select also the first vertex. 
    for i in range(1, len(W_val)+1): C2[i]=C2[i-1]+sum(W_val[i-1])
    #print(C2)

    v = random_select(C2, g.get_adj_list_vertex(u)) 
    # but this should not be selected among all vertices, just among the vertices in the adjacency list!!!
    #print(f"nodes are: {g.get_adj_list_vertex(u).keys()}, bin search selected: {v}")

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
