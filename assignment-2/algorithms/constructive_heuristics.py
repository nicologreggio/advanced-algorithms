from graph.graph import Graph, Vertex, Edge
import random
from typing import Tuple


def min_triangular(k: Vertex, C: list[int], g: Graph) -> "Tuple[int,int]":
    """returns weight of the edge that minimizes "triangleTSP" and the position where the new one should be inserted"""
    min_weight = float("inf")
    for n in range(len(C) - 1):
        i = C[n]
        j = C[n + 1]
        w_ik = g.get_weight(k, i)
        w_kj = g.get_weight(k, j)
        w_ij = g.get_weight(i, j)
        tmp = w_ik + w_kj - w_ij
        if tmp < min_weight:
            min_weight = tmp
            pos = n + 1
    return min_weight, pos


# to randomly select a node which is not in the circuit yet
def random_selection(C: list[int], G: set[int]) -> "Vertex":
    """Select the node according to the random insertion heuristic"""
    c = set(C)
    r = random.choice(list(G - c))
    return r

def init_path(g: Graph, s: Vertex) -> "Tuple[list[int], set[int], int, int]":
    """Initialize circuit for constructive heuristics with node s"""
    d = g.get_adj_list_vertex(s)
    m = min(d, key=d.get)
    G = set(g.get_vertices())
    C = [s, m, s]
    total_len, total_w = g.get_n(), 2 * g.get_weight(s, m)
    return C, G, total_len, total_w

def random_insertion(g: Graph, s: Vertex = 1) -> "list[Vertex]":
    """Return the hamiltonian path built using the random insertion heuristic"""
    C, G, total_len, total_w=init_path(g, s)

    while len(C) <= total_len:
        k = random_selection(C, G)
        w, pos = min_triangular(k, C, g)
        C.insert(pos, k)
        total_w += w
    
    # optionally, total_w (the weight of the circuit) may be returned as well
    return C


def get_dist(k: Vertex, C: list[int], g: Graph) -> "int":
    """Return the circuit-vertex distance between k and C"""
    assert len(C) > 0, f"Cannot calculate distance between {k} and empty circuit!"

    return min([g.get_weight(h, k) for h in C])


def closest_selection(C: list[int], G: set[int], g: Graph) -> "Vertex":
    """Select the node according to the closest insertion heuristic"""
    candidates = G - set(C)
    assert (
        len(candidates) > 0
    ), "{G}\{C} leads to empty set. No candidates available to choose next closest node!"

    min_distance = float("inf")
    for k in candidates:
        new_dist = get_dist(k, C, g)
        if new_dist < min_distance:
            min_distance = new_dist
            r = k

    return r


def closest_insertion(g: Graph, s: Vertex = 1) -> "list[Vertex]":
    """Return the hamiltonian path built using the closest insertion heuristic"""
    C, G, total_len, total_w=init_path(g, s)

    while len(C) <= total_len:
        k = closest_selection(C, G, g)
        w, pos = min_triangular(k, C, g)
        C.insert(pos, k)
        total_w += w

    # optionally, total_w (the weight of the circuit) may be returned as well
    return C
