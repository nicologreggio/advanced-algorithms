import math

from union_find import UnionFind
from graph import Graph


def kruskal_smart(g: Graph):
  mst = []
  uf = UnionFind(g.get_vertices())

  edges = sorted(g.get_edges(), key=lambda edge: edge[1])

  for e in edges:
    vertices, _ = e
    u, v = vertices
    
    if uf.find(u) != uf.find(v):
      mst.append(e)
      uf.union(u, v)

  return mst


def kruskal_smart_behaviour(n, m):
  return m * math.log(n)
