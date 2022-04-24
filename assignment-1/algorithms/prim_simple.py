from collections import defaultdict
import os
import time
import gc
from math import log
from heapq import heappop as hpop
from heapq import heappush as hpush
import matplotlib.pyplot as plt

def prim(g, s):
  inf = float('inf')
  keys, parents, inQ = {}, {}, {}
  for i in g:
    parents[i] = None
    keys[i] = inf
    inQ[i] = 1

  keys[s] = 0
  # Q is a heap since initialized empty and used only with python heapq functions
  # -> this ensures that the heap invariant holds
  Q=[]
  hpush(Q, (0,s)) # Q will contain tuples in the form (key, vertex), sorted by key

  while len(Q) > 0:
    u = hpop(Q)
    inQ[u[1]] = 0
    for k, v in [item for item in g[u[1]].items() if item[0] != 'key' and item[0] != 'parent' and item[0] != 'inQ']:
      # if g[k]['inQ'] and v < g[k]['key']:
      if inQ[k] and v < keys[k]:
        keys[k]=v
        hpush(Q, (v, k))
        parents[k]=u[1]

  return parents, sum(keys.values()) # returns the mst & its weight

def read_file(f):
  h=defaultdict(dict) # automatically creates dict on non-existing keys
  with open(f) as file:
    n, m = file.readline().strip().split(' ')
    lines = file.readlines()
    for line in lines:
      e1, e2, w = line.strip().split(' ')
      h[e1][e2] = int(w)
      h[e2][e1] = int(w)
  return h, int(n), int(m)


# ========================================
path='../dataset-1'
# path='../dataset-2'

assert (os.path.exists(path)), "Not a valid path! (" + path + ")"
os.chdir(path)

print("path chosen: " + os.getcwd())

base_exec = 1000
graph_sizes, run_times, weights = [], [], []

for root, dirs, files in os.walk(os.getcwd()):
  for file in sorted(files):
    if file.endswith(".txt"):
      graph, nodes, edges = read_file(os.path.join(root, file))
      graph_sizes.append([nodes, edges])
      num_exec = int(base_exec / nodes)
      # if num_exec == 0:
      #     num_exec = 10
      num_exec=1000

      gc.disable()
      start = time.perf_counter_ns()
      for _ in range(num_exec):
        mst, mst_weight=prim(graph, '1')
      end = time.perf_counter_ns()
      gc.enable()

      print(mst)
      weights.append(mst_weight)

      avg = int((end - start) / num_exec)
      run_times.append(avg)

""" 
=================== MEASURE RUN TIME
"""
ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(graph_sizes)-1)]
c_estimates = [round(run_times[i]/(graph_sizes[i][1]*log(graph_sizes[i][0])),3) for i in range(len(graph_sizes))]

# trick for right automatic padding can be picking the length of the max element we're going to print & add some spaces
padding=18
headers=[str(h).ljust(padding) for h in['Size','Time(ns)','Costant','Ratio', 'Mst weight']]
hr=padding*(len(headers)+1) * "-"
print('\n\n\n')
print(*headers, sep='\t')
print(hr)
for i in range(len(graph_sizes)):
  print(str(graph_sizes[i]).ljust(padding), 
        str(run_times[i]).ljust(padding), 
        str(c_estimates[i]).ljust(padding), 
        str(ratios[i]).ljust(padding), 
        str(weights[i]).ljust(padding),
        sep="\t")
print(hr)
print("average c: ", (sum(c_estimates) / len(c_estimates)))

# print(f'Time: {end-start}, with {len(graphs)} graphs')
# print('total heap time: ', time_for_heap/(10**9))

C = sum(c_estimates) / len(c_estimates)
# C=330
reference = [C * m*(log(n)) for n,m in graph_sizes]
plt.plot([m*n for n,m in graph_sizes], run_times)
plt.plot([m*n for n,m in graph_sizes], reference)
plt.legend(["Measured time", "c * m*log(n)"])
plt.ylabel('run time (ns)')
plt.xlabel('size')
plt.show()