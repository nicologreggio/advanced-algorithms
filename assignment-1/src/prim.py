from graph import Graph, Vertex
import math

from priority_queue import PriorityQueue
from VertexHelper import VertexHelper


def prim(g: Graph, s: Vertex = 1):
  h = PriorityQueue()

  for v in g.get_vertices():
    vertex = VertexHelper(float('inf') if v != s else 0, v, None)
    h.push(vertex)

  mst = []

  while len(h) != 0:
    u = h.pop()

    mst.append(u)

    adj = g.get_adj_list_vertex(u.get_value())

    for v in adj:
      el = h.get_element(v)
      new_priority = adj[v]

      if el and new_priority < el.get_key():
        el.set_parent(u)
        h.change_priority(el.get_value(), new_priority)

  return mst



def asymptotic_behaviour(m, n):
  return m * math.log(n)
  