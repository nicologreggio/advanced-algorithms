from typing import Tuple
from graph.graph import Graph, Vertex, Edge
from graph.prim_smarter import prim_smarter
from graph.prim_priority_queue import prim_priority_queue
from graph.kruskal_union_find import kruskal_union_find
from graph.kruskal_naive import is_acyclic, kruskal_naive


def DFS_recursive(g: Graph, v: Vertex, visited: "list[bool]") -> "list[Vertex]":
    visited[v] = True
    children = []

    for u in g.get_adj_list_vertex(v).keys():
        if not visited[u]:
            children += DFS_recursive(g, u, visited)

    return [v] + children


def DFS(g: Graph, r: Vertex):
    visited = {i: False for i in g.get_vertices()}
    return DFS_recursive(g, r, visited)


def approximation2_metric_tsp(g: Graph, r: Vertex = 1) -> "list[Vertex]":
    mst = Graph(prim_priority_queue(g))
    H = DFS(mst, r)

    return H + [r]
