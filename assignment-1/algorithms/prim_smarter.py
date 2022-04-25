from graph.graph import Graph, Vertex
from heapq import heappop as hpop
from heapq import heappush as hpush
from math import log

def prim_smarter(g: Graph, s: Vertex = 1):
  inf = float('inf')
  keys, parents, inQ = {}, {}, {}
  for i in g.get_vertices():
    parents[i] = None
    keys[i] = inf
    inQ[i] = 1

  keys[s] = 0
  # Q is a heap since initialized empty and used only with python heapq functions
  # -> this ensures that the heap invariant holds
  Q=[]
  hpush(Q, (0,s)) # Q will contain tuples in the form (key, vertex), sorted by key

  while len(Q):
    u = hpop(Q)
    inQ[u[1]] = 0
    # for k, v in [item for item in g.get_adj_list_vertex(u[1]).items()]:
    for k, v in (g.get_adj_list_vertex(u[1]).items()):
      if inQ[k] and v < keys[k]:
        keys[k]=v
        hpush(Q, (v, k))
        parents[k]=u[1]

  return [(v, k, keys[k]) for k,v in parents.items()] # returns mst in the form of tuples (parent, node, weight)


def prim_smarter_asymptotic_behaviour(n, m):
  return m * log(n)