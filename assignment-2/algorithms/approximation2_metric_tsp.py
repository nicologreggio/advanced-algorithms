from graph.graph import Graph, Vertex
from graph.prim_priority_queue import prim_priority_queue


def preorder_visit_recursive(
    g: Graph, v: Vertex, visited: "list[bool]"
) -> "list[Vertex]":
    visited[v] = True
    children = []

    for u in g.get_adj_list_vertex(v):
        if not visited[u]:
            children += preorder_visit_recursive(g, u, visited)

    return [v] + children


def preorder_visit(g: Graph, r: Vertex) -> "list[Vertex]":
    if g.get_n() == 0:
        return []

    visited = {i: False for i in g.get_vertices()}
    return preorder_visit_recursive(g, r, visited)


def approximation2_metric_tsp(g: Graph, r: Vertex = 1) -> "list[Vertex]":
    if g.get_n() == 0:
        return []

    mst = Graph(prim_priority_queue(g))
    H = preorder_visit(mst, r)

    return H + [r]
