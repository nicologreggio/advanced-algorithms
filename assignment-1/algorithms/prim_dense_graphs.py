from graph.graph import Graph, Vertex, Edge
from math import log


def min_weight(g: Graph, weights, in_mst):
    min_weight = float("inf")
    min_v = None
    for u in g.get_vertices():
        if not in_mst[u] and weights[u] < min_weight:
            min_weight = weights[u]
            min_v = u

    return min_v


def prim_dense_graphs(g: Graph, s: Vertex = 1) -> "list[Edge]":
    parents = {}
    weights = {}
    in_mst = {}

    for t in g.get_vertices():
        parents[t] = None
        weights[t] = float("inf")
        in_mst[t] = False

    weights[s] = 0

    for _ in g.get_vertices():
        u = min_weight(g, weights, in_mst)

        in_mst[u] = True

        for v in g.get_vertices():
            w = g.get_weight(u, v)

            if w and not in_mst[v] and w < weights[v]:
                parents[v] = u
                weights[v] = w

    return [(v, k, weights[k]) for k, v in parents.items() if v]


def prim_dense_graphs_asymptotic_behaviour(n, _):
    return n ^ 2
