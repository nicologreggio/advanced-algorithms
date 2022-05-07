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


def approximation2_metric_tsp(g: Graph, r: Vertex = 1) -> "list[Edge]":
    mst = prim_priority_queue(g)
    # print(Graph(mst))
    mst = Graph(mst)

    vertices = DFS(mst, r)
    # print(vertices)

    # last_vertex = vertices[-1]
    # H = []
    # for v in vertices:
    #     H.append((last_vertex, v, g.get_weight(last_vertex, v)))
    #     last_vertex = v

    # return H

    H = DFS(mst, r)

    return H + [r]
