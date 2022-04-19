import math

from union_find.union_find import UnionFind
from graph.graph import Edge, Graph


def kruskal_smart(g: Graph) -> list[Edge]:
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


def kruskal_smart_behaviour(n: int, m: int):
  return m * math.log(n)
