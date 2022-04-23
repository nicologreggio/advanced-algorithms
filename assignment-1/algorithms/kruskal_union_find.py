import math

from union_find.union_find import UnionFind
from graph.graph import Edge, Graph


def kruskal_union_find(g: Graph) -> list[Edge]:
  mst = []
  uf = UnionFind(g.get_vertices())

  edges = sorted(g.get_edges(), key = lambda edge: edge[2])

  for e in edges:
    u, v, _ = e
    
    if uf.find(u) != uf.find(v):
      mst.append(e)
      uf.union(u, v)

  return mst


def kruskal_union_find_asymptotic_behaviour(n: int, m: int):
  return m * math.log(n)
