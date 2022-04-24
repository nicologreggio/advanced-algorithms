from graph.graph import Edge, Graph, Vertex
import math

from priority_queue.priority_queue import PriorityQueue
from priority_queue.vertex_helper import VertexHelper

def prim_priority_queue(g: Graph, s: Vertex = 1) -> 'list[Edge]':
  Q = PriorityQueue()
  mst = []

  for v in g.get_vertices():
    Q.insert(VertexHelper(v, float('inf') if v != s else 0, None))

  while len(Q):
    u = Q.extract_min()

    if u.get_parent():
      mst.append((u.get_parent().get_name(), u.get_name(), u.get_priority()))

    adj = g.get_adj_list_vertex(u.get_name())

    for v in adj:
      i = Q.get_index(v)
      if i != -1:
        vertex = Q.get_element(i)
        new_priority = adj[v]

        if new_priority < vertex.get_priority():
          vertex.set_parent(u)
          Q.decrease_key(i, new_priority)
    
  return mst


def prim_priority_queue_asymptotic_behaviour(n: int, m: int):
  return m * math.log(n)
