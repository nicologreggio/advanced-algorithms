import math
from typing import Set, Tuple

from fibheap.fibheap import FibHeap
from fibheap.fibheap_item import FibHeapItem
import copy

from graph.graph import Graph, Vertex


def st_min_cut(g: Graph) -> Tuple[Tuple[Set[Vertex], Set[Vertex]], Vertex, Vertex]:
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


def compute_cut_weight(g: Graph, V1: Set[Vertex], t: Set[Vertex]) -> int:
    w = 0

    (t,) = t
    for v in V1:
        w += g.get_weight(v, t)

    return w


def stoer_wagner(g: Graph) -> Tuple[Set[Vertex], Set[Vertex]]:
    # assert g.get_n() < 2, "The graph needs to have at least 2 vertices"

    if g.get_n() == 2:
        s, t = g.get_vertices()
        return (set([s]), set([t]))
    else:
        C1, s, t = st_min_cut(g)
        g.contract_edge(s, t)
        g = copy.deepcopy(g)
        C2 = stoer_wagner(g)

        print("Cut 1: ", C1, compute_cut_weight(g, *C1))
        print("Cut 2: ", C2, compute_cut_weight(g, *C2))

        if compute_cut_weight(g, *C1) <= compute_cut_weight(g, *C2):
            return C1
        else:
            return C2


def stoer_wagner_asymptotic_behaviour(n: int, m: int) -> int:
    return m * n + n ** 2 * math.log(n)
