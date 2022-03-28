from dataclasses import Field, dataclass
import functools
import matplotlib.pyplot as plt
import math
import heapq as hq
import numpy as np

from graph import Graph, Vertex, group_all_files, init_args, init_graph_from_file, init_graph_from_files, init_graphs_from_grouped_files, read_sort_files
from asymptotic_behaviour import compute_asymptotic_constant, map2, compute_asymptotic_constant_light
from priority_queue import PriorityQueue


class VertexHelper:
  def __init__(self, priority, v, parent):
    self._priority = priority
    self._v = v
    self._parent = parent

  def get_key(self):
    return self._priority

  def get_value(self):
    return self._v

  def set_parent(self, p):
    self._parent = p

  def set_priority(self, priority):
    self._priority = priority

  def __lt__(self, other):
      return self._priority < other._priority

  def __str__(self):
    return f'({self._priority}, {self._v}, {self._parent.get_value() if self._parent else None})'

  def __repr__(self):
    return self.__str__()


def prim_personal_impl(g: Graph, s: Vertex = 1):
  h = PriorityQueue()

  for v in g.get_vertices():
    vertex = VertexHelper(float('inf') if v != s else 0, v, None)
    h.push(vertex)

  mst = []

  while len(h) != 0:
    u = h.pop()

    mst.append(u)

    adj = g.get_adj(u.get_value())

    for v in adj:
      el = h.get_element(v)
      new_priority = adj[v]

      if el and new_priority < el.get_key():
        el.set_parent(u)
        h.change_priority(el.get_value(), new_priority)

  return mst


def prim_internet_impl(g: Graph, s: Vertex = 1):
  active_edges=[]

  mst = []
  in_mst={i:False for i in g.get_vertices()}

  s = VertexHelper(0, s, -1)
  hq.heappush(active_edges, s)

  while active_edges:
    node = hq.heappop(active_edges)
    
    mst.append(node)
    in_mst[node.get_value()]=True

    adj = g.get_adj(node.get_value())
    
    for v in adj:
      w = adj[v]
      if not in_mst[v]:
          hq.heappush(active_edges, VertexHelper(w, v, node.get_value()))
  
  return mst


def prim_asymptotic_behaviour(n, m):
  return m * math.log(n, 2)


def plot_complexity(c, graphs_dimensions, run_times, asymptotic_behaviour):
  ax = plt.axes(projection='3d')

  x = np.asarray([n for (n, _) in graphs_dimensions])
  y = np.asarray([m for (_, m) in graphs_dimensions])

  reference_z = np.asarray([c * asymptotic_behaviour(n, m) for (n, m) in graphs_dimensions])

  ax.plot(x, y, reference_z, 'C1', label='C1')
  ax.plot(x, y, np.asarray(run_times), 'C2', label='C2')
  ax.legend()
  plt.show()


def main():
  args = init_args().parse_args()

  files = read_sort_files(args.d)

  # run_times, ratios, c_estimates = compute_asymptotic_constant(prim, prim_asymptotic_behaviour, graphs, num_calls)

  graphs_dimensions, run_times, ratios, c_estimates = compute_asymptotic_constant_light(
    prim_internet_impl, 
    prim_asymptotic_behaviour, 
    files,
    init_graph_from_file,
    10
  )

  print(run_times)
  print(c_estimates)

  print("Size\t\tTime(ns)\t\tCostant\t\tRatio")
  print(90*"-")
  for i in range(len(c_estimates)):
    print(f'{graphs_dimensions[i][0]}*log({graphs_dimensions[i][1]})', run_times[i], '', c_estimates[i], '', ratios[i], sep="\t")
  print(90*"-")

  # Plot

  c = sum(c_estimates)/len(c_estimates)

  plot_complexity(c, graphs_dimensions, run_times, prim_asymptotic_behaviour)
  # print(prim_personal_impl(init_graph_from_file(args.f)))


if __name__ == "__main__":
  main()
