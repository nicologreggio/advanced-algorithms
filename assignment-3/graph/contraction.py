from typing import List
from graph.graph import Graph, Vertex
from random import randrange
from math import ceil, sqrt


def get_nth_vertex(d, nth: int):  # d is a list of keys (list[Vertex]?)
    # now should work with e-1
    """returns the nth vertex, starting from 0"""
    assert nth < len(d), f"dictionary has {len(d)} vertices, so {nth} is out of bounds"
    it = iter(d)
    for _ in range(0, nth):
        next(it)
    return next(it)


def binary_search(C: List[int], r: int):
    """returns an int if found, None if not found."""
    # NB: in our case should never return None, because we're choosing r exactly in the correct range.
    # start, next, end = 0, None, len(C) - 1
    start, next, end = 0, None, len(C)
    found = False
    while start < end and not found:
        next = (start + end) // 2
        if C[next - 1] <= r and r < C[next]:
            found = True
        elif C[next - 1] <= r:
            start = next + 1
        else:
            end = next
    return next if found else None


# def random_select(g: Graph, C: List[int]) -> Vertex: #(g: Graph, C: List[int]) -> Edge:
def random_select(C: List[int], d) -> Vertex:  # d should be a list of keys
    r = randrange(0, C[-1])  # I don't want to have the last one included
    e = binary_search(C, r)
    return get_nth_vertex(d, e - 1)


def edge_select(g: Graph):
    D = g.get_weighted_degree_list()

    D_val = list(D.values())
    # C1 = [sum(D_val[:i]) for i in range(1, len(D_val) + 1)]
    C1 = [0] + [sum(D_val[:i]) for i in range(1, len(D_val) + 1)]
    # should start from 0, in order to be able to select also the first vertex.

    u = random_select(C1, g.get_vertices())

    W_val = list(g.get_adj_list_vertex(u).values())

    C2 = [None] * (len(W_val) + 1)
    C2[0] = 0
    # also this should start from 0, in order to be able to select also the first vertex.
    for i in range(1, len(W_val) + 1):
        C2[i] = C2[i - 1] + sum(W_val[i - 1])

    v = random_select(C2, g.get_adj_list_vertex(u))
    # but this should not be selected among all vertices, just among the vertices in the adjacency list!!!

    return (u, v)


def contract_edge(graph: Graph, u: Vertex, v: Vertex) -> Graph:
    """Returns a new graph with the (u,v) edge contracted"""
    g = Graph(graph.get_edges())
    g.remove_edge(u, v)

    for w in g.get_vertices():
        if w != u and w != v:
            weight = g.get_weight(w, v)
            if weight != 0:
                g.add_edge(u, w, weight)
                g.remove_edge(w, v)

    g.remove_vertex(v)

    return g


def contract(graph: Graph, k: int) -> Graph:
    """Returns a new graph contracted to k vertices"""
    g = graph
    n = graph.get_n()
    for _ in range(1, n + 1 - k):
        u, v = edge_select(g)  # should use the updated graph!
        g = contract_edge(g, u, v)
    return g


def recursive_contract(g: Graph) -> int:
    n = g.get_n()
    if n <= 6:
        g = contract(g, 2)
        s, t = g.get_vertices()
        w = g.get_weight(s, t)
        return w

    t = ceil(n / sqrt(2) + 1)
    ws = []
    for _ in range(2):
        g_tmp = contract(g, t)
        ws.append(recursive_contract(g_tmp))

    return min(ws)
