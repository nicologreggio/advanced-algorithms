import sys
import os
import functools
import time
import gc
from math import log
import heapq
from heapq import heappop as hpop
from unicodedata import numeric


def prim(g, s):
  # build Q as heap
  # since python sorts heap based on list or list of tuples considering the first element,
  # must be build a list of keys:node with keys initially inf
  # print(f'\n\n*******\n<DOING STUFF WITH{g}')
  inf = float('inf')
  for i in g:
    g[i]['parent'] = None
    g[i]['key'] = [inf]
  Q = [(g[i]['key'], i) for i in list(g.keys())]
  g[s]['key'][0] = 0
  heapq.heapify(Q)

  while len(Q) > 0:
    u = hpop(Q)
    # print('adjacent of ', u, ' are ', g[u[1]])
    for v in [
      item for item in g[u[1]] if item != 'key' and item != 'parent'
    ]:
      for key, i in Q:
        # print(i,'==',v,' and ',int(g[u[1]][v]),' < ', key[0])
        if i == v and int(g[u[1]][v]) < key[0]:
          key[0] = int(g[u[1]][v])
          g[v]['parent'] = u[1]
    heapq.heapify(Q)


def read_file(f):
  h = {}
  with open(f) as file:
    # nodes, edges = file.readline().strip().split(' ')
    # print(f'There are {nodes} nodes and {edges} edges')
    n, m = file.readline().strip().split(' ')
    lines = file.readlines()
    for line in lines:
      # print(line)
      e1, e2, w = line.strip().split(' ')
      # print(f'({e1}, {e2}) {w}')
      if e1 not in h:
        h[e1] = {}
      if e2 not in h:
        h[e2] = {}
      h[e1][e2] = w
      h[e2][e1] = w
  return h, int(n), int(m)


# ========================================
# path='../dataset-1'
path = 0
if not path:
    path = '.'

# os.path.relpath()  -> to get relative path
# os.path.abspath() ...
# os.getcwd() -> print working dir
assert (os.path.exists(path)), "Not a valid path! (" + path + ")"
os.chdir(path)

print("path chosen: " + os.getcwd())
base_exec = 1000
graph_sizes = []
avgs = []
# print('File\t Avg')
# print('-'*20)
for root, dirs, files in os.walk(os.getcwd()):
  for file in files:
    if file.endswith(".txt"):
      # print(os.path.join(root, file))
      graph, nodes, edges = read_file(os.path.join(root, file))
      graph_sizes.append([nodes, edges])
      num_exec = int(base_exec / nodes)
      if num_exec == 0:
          num_exec = 1

      gc.disable()
      start = time.perf_counter_ns()
      for _ in range(num_exec):
          prim(graph, '1')
      end = time.perf_counter_ns()
      gc.enable()

      avg = int((end - start) / num_exec)
      avgs.append(avg)
      # print(graphs, '\t', avg)
      # graphs.append(graph)
      # mst={k: v['parent'] for k,v in graph.items()}
      # print('we have ',mst)

ratios = [None] + [
  round(avgs[i + 1] / avgs[i], 3) for i in range(len(graph_sizes) - 1)
]
c_estimates = [
  round(avgs[i] / log(graph_sizes[i]), 3) for i in range(len(graph_sizes))
]

print("Size\tTime(ns)\tCostant\t\tRatio")
print(50 * "-")
for i in range(len(graph_sizes)):
  print(graph_sizes[i], avgs[i], '', c_estimates[i], '', ratios[i], sep="\t")
print(50 * "-")
print("average c: ", (sum(c_estimates) / len(c_estimates)))

# print(f'Time: {end-start}, with {len(graphs)} graphs')