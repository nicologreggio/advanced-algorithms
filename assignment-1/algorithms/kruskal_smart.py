import math

from union_find.union_find import UnionFind
from graph.graph import Edge, Graph


def kruskal_smart(g: Graph) -> list[Edge]:
  mst = []
  uf = UnionFind(g.get_vertices())

  edges = sorted(g.get_edges(), key=lambda edge: edge[1])

  for e in edges:
    vertices, _ = e
    v, w = vertices
    
    if uf.find(v) != uf.find(w):
      mst.append(e)
      uf.union(v, w)

  return mst


def kruskal_smart_behaviour(n: int, m: int):
  return m * math.log(n)
