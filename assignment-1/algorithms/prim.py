from graph.graph import Edge, Graph, Vertex
import math

from priority_queue.priority_queue import PriorityQueue
from priority_queue.vertex_helper import VertexHelper
from sortedcontainers import SortedDict, SortedList, SortedSet

def prim(g: Graph, s: Vertex = 1) -> list[Edge]:
  pq = SortedSet()
  inf = float('inf')
  vertices = {}
  mst = []

  for v in g.get_vertices():
    vertex = VertexHelper(v, inf if v != s else 0, None)
    vertices.update({v: vertex})
    pq.add(vertex)

  while len(pq):
    u = pq.pop(0)
    vertices.pop(u.get_value())

    if u.get_parent():
      mst.append((u.get_parent(), u.get_value(), u.get_priority()))

    adj = g.get_adj_list_vertex(u.get_value())

    for v in adj:
      vertex = vertices.get(v, None)
      new_priority = adj[v]

      if vertex and new_priority < vertex.get_priority():
        pq.remove(vertex)
        vertex.change_priority(new_priority)
        vertex.set_parent(u.get_value())
        pq.add(vertex)
    
  return mst


def prim_behaviour(n: int, m: int):
  return m * math.log(n)
