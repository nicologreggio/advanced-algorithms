from graph.graph import Graph, Vertex
import math
from priority_queue.vertex_helper import VertexHelper
from priority_queue.priority_queue import PriorityQueue

import heapq as hq

def prim(g: Graph, s: Vertex = 1):
  if g.get_n() <= 0: return []

  active_edges = []

  mst = []
  in_mst={i:False for i in g.get_vertices()}

  s = VertexHelper(0, s, None)
  hq.heappush(active_edges, s)

  while len(mst) != g.get_n() - 1:
    node = hq.heappop(active_edges)

    if not in_mst[node.get_value()]:
      if node.get_parent():
        mst.append((node.get_parent().get_value(), node.get_value(), node.get_priority()))
      
      in_mst[node.get_value()] = True

      adj = g.get_adj_list_vertex(node.get_value())
      
      for v in adj:
        if not in_mst[v]:
            hq.heappush(active_edges, VertexHelper(adj[v], v, node))
  
  return mst


def prim_behaviour(n, m):
  return m * math.log(n)