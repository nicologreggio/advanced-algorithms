from collections import defaultdict
from glob import glob
from typing import NewType, Tuple
import heapq as hq

from tsp.tsp_file import TSPEdgeWeightType, TSPFileLabel
from tsp.points import init_point


GRAPH_FILE_EXTENSION = "tsp"

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
        return self.adj_list[s].get(t)

    def get_n(self):
        """returns the number of nodes"""
        return len(self.adj_list)

    def get_m(self):
        """returns the number of edges"""
        return len(self.edges)

    def get_information(self, key):
        return self.information.get(key, None)

    def add_edge(self, s: Vertex, t: Vertex, w):
        """adds an edge between the vertices s and t with weight w"""
        self.adj_list[s][t] = w
        self.adj_list[t][s] = w

        self.edges.add((s, t, w))

    def remove_edge(self, s: Vertex, t: Vertex):
        w = self.adj_list[s][t]

        if t in self.adj_list[s]:
            del self.adj_list[s][t]

        if s in self.adj_list[t]:
            del self.adj_list[t][s]

        self.edges.discard((s, t, w))
        self.edges.discard((t, s, w))

    def __repr__(self):
        return "(V: {0}, E: {1})".format(self.get_n(), self.get_m())


def read_tsp_graph(f) -> "Tuple[Graph, int]":
    file_information = {}

    s = next(f).strip()
    while s and s != TSPFileLabel.NODE_COORD_SECTION.value:
        information, value = list(map(lambda s: s.strip(), s.split(":")))
        file_information[TSPFileLabel[information]] = value

        s = next(f).strip()

    data = {}
    vertices = []
    s = next(f).strip()
    while s and s != TSPFileLabel.EOF.value:
        line = s.split()
        v, x, y = int(line[0]), float(line[1]), float(line[2])
        data[v] = init_point(
            x,
            y,
            TSPEdgeWeightType[file_information[TSPFileLabel.EDGE_WEIGHT_TYPE]],
        )
        hq.heappush(vertices, v)

        s = next(f).strip()

    g = Graph([], file_information)
    for i, s in enumerate(vertices):  # [(0, 32), (1, 54), (2, 55), (3, 56), (4, 57)]
        for t in vertices[i + 1 :]:  # [54, 55, 56, 57]
            p_s = data[s]
            p_t = data[t]
            g.add_edge(s, t, p_s.compute_distance(p_t))

    # TODO: write in the report that the parameter optimal solution has been added to the dataset files
    return (g, int(file_information[TSPFileLabel.OPTIMAL_SOLUTION]))


def open_tsp_graph(file_path):
    with open(file_path, "r") as f:
        return read_tsp_graph(f)


def read_all(directory_path, size=None):
    files = read_sort_files(directory_path, size)
    return list(map(open_tsp_graph, files))


def read_sort_files(directory_path, size=None):
    files = sorted(glob(f"{directory_path}/*.{GRAPH_FILE_EXTENSION}"))
    return files if not size else files[:size]
