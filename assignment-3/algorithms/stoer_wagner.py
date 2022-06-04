import math
from typing import Set, Tuple

from fibheap.fibheap import FibHeap
from fibheap.fibheap_item import FibHeapItem
import copy

from graph.graph import Graph, Vertex, Cut


def st_min_cut(g: Graph) -> Tuple[Cut, Vertex, Vertex]:
    PQ = FibHeap()
    keys = {}
    vertices = {}
    in_pq = {}

    for v in g.get_vertices():
        keys[v] = 0
        vertices[v] = FibHeapItem(v, keys[v])
        in_pq[v] = True
        PQ.insert(vertices[v])

    s = None
    t = None

    E = g.get_edges()
    while len(PQ):
        u = PQ.extract_maximum()
        in_pq[u.name] = False
        s = t
        t = u.name

        for u, v, w in E:
            if in_pq[v]:
                keys[v] = keys[v] + w
                PQ.increase_key(vertices[v], keys[v])

    V = set(g.get_vertices())
    return ((V - set([t]), set([t])), s, t)


def compute_cut_weight(g: Graph, C: Cut) -> int:
    w = 0
    V, (t,) = C

    for v in V:
        w += g.get_weight(v, t)

    return w


def stoer_wagner(g: Graph) -> int:
    if g.get_n() == 2:
        s, t = g.get_vertices()
        C = (set([s]), set([t]))
        print("Final Cut: ", C, compute_cut_weight(g, C))
        return compute_cut_weight(g, C)
    else:
        C1, s, t = st_min_cut(g)
        C1_w = compute_cut_weight(g, C1)

        g1 = g.contract_edge(s, t)

        C2_w = stoer_wagner(g1)
        # C2_w = compute_cut_weight(g1, C2)

        print("s, t", (s, t))
        print("Cut 1: ", C1, C1_w)
        print("Cut 2: ", C2_w)

        if C1_w <= C2_w:
            return C1_w
        else:
            return C2_w


def stoer_wagner_asymptotic_behaviour(n: int, m: int) -> int:
    return m * n + n ** 2 * math.log(n)
