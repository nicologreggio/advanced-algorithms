from numpy import infty
from tsp.tsp_file import *
from tsp.points import *
from graph.graph import *
import random

# k has been randomly selected 
# C is the partial circuit: has starting point repeated at the end 
# g is the graph 
def min_triangular(k, C, g): 
    p_min = float(infty)
    for n in range(len(C)-1):
        i = C[n]
        j = C[n+1] 
        w_ik = g.get_adj_list_vertex(k)[i]
        w_kj = g.get_adj_list_vertex(k)[j]
        w_ij = g.get_adj_list_vertex(i)[j]
        tmp = w_ik + w_kj - w_ij
        if tmp < p_min: 
            p_min = tmp 
            ins = n +1
    return p_min, ins

# to randomly select a node which is not in the circuit yet 
def random_selection(C, G): 
    c = set(C)
    r = random.choice(list(G - c))
    return r 

def random_insertion(g): 
    d = g.get_adj_list_vertex(1)
    m = min(d, key=d.get)
    G = set(g.get_vertices())
    C = [1, m, 1]
    w = 2*g.get_adj_list_vertex(1)[m]
  
    while len(C) < g.get_n() + 1:
        k = random_selection(C, G)
        tmp, ins = min_triangular(k, C, g)
        C.insert(ins, k)
        w = w + tmp
    return C, int(w) 



