from collections import defaultdict
from glob import glob
from typing import NewType, Tuple
import heapq as hq

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)


class Graph:
    def __init__(self, edges: "list[Edge]" = [], information={}):
        self.adj_list = defaultdict(lambda: defaultdict(list))
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

        self.edges.add((s, t, w))
        self.edges.add((t, s, w))

    def merge_vertices(self, s: Vertex, t: Vertex):
        print("Merging: ", s, t)

        s_adj_list = self.adj_list.pop(s)
        t_adj_list = self.adj_list.pop(t)

        for v, ws in s_adj_list.items():
            if v != t:
                del self.adj_list[v][s]
            for w in ws:
                self.edges.remove((v, s, w))
                self.edges.remove((s, v, w))

        for v, ws in t_adj_list.items():
            if v != s:
                del self.adj_list[v][t]
                for w in ws:
                    self.edges.remove((v, t, w))
                    self.edges.remove((t, v, w))

        s_adj_list.pop(t)
        t_adj_list.pop(s)

        new_vertex = s

        print(f"Adj list {s}: ", s_adj_list)
        print(f"Adj list {t}: ", t_adj_list)

        for v, ws in s_adj_list.items():
            for w in ws:
                print("Adding: ", (v, new_vertex, w))
                self.add_edge(v, new_vertex, w)

        for v, ws in t_adj_list.items():
            for w in ws:
                w_from_s = sum(s_adj_list.get(v, []))
                print("Adding: ", (v, new_vertex, w + w_from_s))
                self.add_edge(v, new_vertex, w)

        print("Vertices: ", self.get_vertices())
        print("Edges: ", self.get_edges())

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
