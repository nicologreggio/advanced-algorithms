from graph.graph import Graph, Vertex
import random
from typing import Tuple

'''INITIALIZATION: common subroutine'''

def init_path(g: Graph, s: Vertex) -> "Tuple[list[int], set[int], int, int]":
    """Initialize circuit for constructive heuristics with node s"""
    d = g.get_adj_list_vertex(s)
    m = min(d, key=d.get)
    G = set(g.get_vertices()) # set of vertices
    C = [s, m, s] # build the single node path
    
    # the num. of vertices the circuit will need to have and the initial weight of the path
    total_len, total_w = g.get_n(), 2 * g.get_weight(s, m) 
    return C, G, total_len, total_w
    


'''SELECTION: random vs. closest '''   

def random_selection(C: list[int], G: set[int]) -> "Vertex":
    """Select the node according to the random insertion heuristic"""
    c = set(C)
    r = random.choice(list(G - c))
    return r    


def get_dist(k: Vertex, C: list[int], g: Graph) -> "int":
    """Return the circuit-vertex distance between k and C"""
    assert len(C) > 0, f"Cannot calculate distance between {k} and empty circuit!"

    # since C is a list here, the start and end of the path will be used twice in the following calculation
    # but the overhead of converting C to a Set here each time is not worth, 
    # since neither computation nor result are affected
    return min([g.get_weight(h, k) for h in C]) 

def closest_selection(C: list[int], G: set[int], g: Graph) -> "Vertex":
    """Select the node according to the closest insertion heuristic
    :param list[int] C: circuit
    :param set[int] G: set of nodes of the graph g
    :param Graph g: the graph"""

    candidates = G - set(C) # vertices not in the circuit yet
    assert (
        len(candidates) > 0
    ), "{G}\{C} leads to empty set. No candidates available to choose next closest node!"

    min_distance = float("inf")
    # for each k not in the circuit calculate its cirucit-vertex distance from C
    for k in candidates:
        new_dist = get_dist(k, C, g)
        if new_dist < min_distance:
            min_distance = new_dist
            r = k

    return r # this is the k not in C that minimizes ciruit-vertex distance



'''INSERTION: common subroutine'''

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



'''ALGORITHMS'''

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
