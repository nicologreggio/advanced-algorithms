import math
from fibheap.fibheap import FibHeap
from fibheap.fibheap_item import FibHeapItem


def stoer_wagner(g):
    PQ = FibHeap.make_fibheap()
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
        t = u

        for u, v, w in E:
            if in_pq[v]:
                keys[v] = keys[v] + w
                PQ.increase_key(vertices[v], keys[v])

    V = set(g.get_vertices())
    return ((V - set([t]), t), s, t)


def stoer_wagner_asymptotic_behaviour(n, m):
    return m * n + n ** 2 * math.log(n)
