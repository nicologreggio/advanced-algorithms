from graph.graph import Graph, Vertex, Edge


def min_triangular(k, C, g: Graph):
    min_weight = float("inf")
    for n in range(len(C) - 1):
        i = C[n]
        j = C[n + 1]
        w_ik = g.get_adj_list_vertex(k)[i] #todo change to get_weight & test
        w_kj = g.get_adj_list_vertex(k)[j]
        w_ij = g.get_adj_list_vertex(i)[j]
        tmp = w_ik + w_kj - w_ij
        if tmp < min_weight:
            min_weight = tmp
            pos = n + 1
    return min_weight, pos

def get_dist(k, C, g: Graph):
    min_distance=float('inf')
    r=C[0]
    for c in C:
        d=g.get_adj_list_vertex(c)[k]
        if d<min_distance:
            r=c
            min_distance=d

    return c


def closest_selection(C, G, g):
    candidates=G-set(C)
    min_distance=float('inf')
    r=list(candidates)[0]
    for k in candidates:
        new_dist=get_dist(k, C, g)
        if new_dist<min_distance: 
            min_distance=new_dist
            r=k

    return k


def closest_insertion(g: Graph, s: Vertex = 1) -> "list[Edge]":
    d = g.get_adj_list_vertex(s)
    m = min(d, key=d.get)
    G = set(g.get_vertices())
    C = [s, m, s]
    w = 2 * g.get_adj_list_vertex(s)[m]

    total_len, total_w = g.get_n(), 0

    while len(C) <= total_len:
        k = closest_selection(C, G, g)
        w_min, pos = min_triangular(k, C, g)
        C.insert(pos, k)
        total_w += w_min

    return C#, total_w
