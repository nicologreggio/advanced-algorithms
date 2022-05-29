from collections import defaultdict
from glob import glob
from typing import NewType, Tuple
import heapq as hq

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)


class Graph:
    def __init__(self, edges: "list[Edge]" = [], information={}):
        self.adj_list = defaultdict(dict)
        self.edges = set()
        self.information = information

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
        return self.adj_list[s].get(t, None)

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
        self.adj_list[s][t] = w
        self.adj_list[t][s] = w

        self.edges.add((s, t, w))
        self.edges.add((t, s, w))

    def merge_vertices(self, s: Vertex, t: Vertex):
        s_adj_list = self.adj_list.pop(s)
        t_adj_list = self.adj_list.pop(t)

        for v, w in s_adj_list.items():
            if v != t:
                del self.adj_list[v][s]
            self.edges.remove((v, s, w))
            self.edges.remove((s, v, w))

        for v, w in t_adj_list.items():
            if v != s:
                del self.adj_list[v][t]
                self.edges.remove((v, t, w))
                self.edges.remove((t, v, w))

        new_vertex = s

        for v, w in s_adj_list.items():
            if t != v:
                self.add_edge(v, new_vertex, w)

        for v, w in t_adj_list.items():
            if s != v:
                self.add_edge(v, new_vertex, w)

        print(self.get_vertices(), s, t)

    def remove_edge(self, s: Vertex, t: Vertex):
        """removes the edge from s to t and vice-versa"""
        w = self.adj_list[s].get(t, None)

        if w != None:
            if t in self.adj_list[s]:
                del self.adj_list[s][t]

            if s in self.adj_list[t]:
                del self.adj_list[t][s]

            self.edges.discard((s, t, w))
            self.edges.discard((t, s, w))

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())
