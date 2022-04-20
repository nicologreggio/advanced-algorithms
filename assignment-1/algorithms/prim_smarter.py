from graph import Graph, Vertex
import math
from priority_queue.VertexHelper import VertexHelper

import heapq as hq

def prim(g: Graph, s: Vertex = 1):
  active_edges=[]

  mst = []
  in_mst={i:False for i in g.get_vertices()}

  s = VertexHelper(0, s, -1)
  hq.heappush(active_edges, s)

  while active_edges:
    node = hq.heappop(active_edges)
    
    mst.append(node)
    in_mst[node.get_value()]=True

    adj = g.get_adj_list_vertex(node.get_value())
    
    for v in adj:
      w = adj[v]
      if not in_mst[v]:
          hq.heappush(active_edges, VertexHelper(w, v, node))
  
  return mst


def asymptotic_behaviour(n, m):
  return m * math.log(n)