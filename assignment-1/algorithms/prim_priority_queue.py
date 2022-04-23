from graph.graph import Edge, Graph, Vertex
import math

from priority_queue.priority_queue import PriorityQueue
from priority_queue.vertex_helper import VertexHelper

def prim_priority_queue(g: Graph, s: Vertex = 1) -> list[Edge]:
  pq = PriorityQueue()
  inf = float('inf')
  mst = []

  for v in g.get_vertices():
    vertex = VertexHelper(v, inf if v != s else 0, None)
    pq.insert(vertex)

  while len(pq):
    u = pq.extract_min()

    if u.get_parent():
      mst.append((u.get_parent(), u.get_value(), u.get_priority()))

    adj = g.get_adj_list_vertex(u.get_value())

    for v in adj:
      i = pq.get_index(v)
      if i != -1:
        vertex = pq.get_element(i)
        new_priority = adj[v]

        if new_priority < vertex.get_priority():
          vertex.set_parent(u.get_value())
          pq.decrease_key(i, new_priority)
    
  return mst


def prim_priority_queue_asymptotic_behaviour(n: int, m: int):
  return m * math.log(n)
