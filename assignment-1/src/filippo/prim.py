import matplotlib.pyplot as plt
import math
import heapq as hq
import numpy as np

from graph import Graph, Vertex, group_all_files, init_args, init_graph_from_file, init_graph_from_files, init_graphs_from_grouped_files, read_sort_files
from asymptotic_behaviour import compute_asymptotic_constant, compute_asymptotic_constant_light


def prim(g: Graph, s: Vertex = 1):
  h = list(map(lambda v: (float('inf'), v, -1), filter(lambda v: v != s, g.get_vertices())))

  '''
  def reduce_function(acc, v):
    acc.update(v);
    return acc

  h = functools.reduce(
    lambda acc, v:
      acc.update(v); acc
    ,
    map(lambda v: {v: (float('inf'), -1)}, filter(lambda v: v != s, g.get_vertices())),
    {}
  )
  '''

  s = (0, s, -1)
  hq.heappush(h, s)

  mst = []

  def getFromHeap(h, v):
    return next(((i, x) for i, x in enumerate(h) if x[1] == v), (-1, None))

  while h:
    hq.heapify(h)

    u = hq.heappop(h)
    mst.append(u)

    adj = g.get_adj(u[1])


    for v in adj:
      x = getFromHeap(h, v)

      i, vHeap = x

      if vHeap and adj[v] < vHeap[0]:
        l = list(vHeap)

        l[0] = adj[v]
        l[2] = u[1]

        h[i] = tuple(l)

  return mst


def prim_asymptotic_behaviour(n, m):
  return m * math.log(n)


def plot_complexity(c, graphs_dimensions, run_times, asymptotic_behaviour):
  fig = plt.figure()
  ax = plt.axes(projection='3d')

  x = np.asarray([n for (n, _) in graphs_dimensions])
  y = np.asarray([m for (_, m) in graphs_dimensions])

  reference_z = np.asarray([c * asymptotic_behaviour(n, m) for (n, m) in graphs_dimensions])

  ax.plot(x, y, reference_z)

  ax.plot(x, y, np.asarray(run_times))

  # plt.plot(list_sizes, run_times)
  # plt.plot(list_sizes, reference)
  # plt.legend(["Measured time", "69 * N"])
  # plt.ylabel('run time (ns)')
  # plt.xlabel('size')
  plt.show()


def main():
  args = init_args().parse_args()

  files = read_sort_files(args.d)[:24]

  # run_times, ratios, c_estimates = compute_asymptotic_constant(prim, prim_asymptotic_behaviour, graphs, num_calls)

  graphs_dimensions, run_times, ratios, c_estimates = compute_asymptotic_constant_light(prim, prim_asymptotic_behaviour, files, init_graph_from_file)

  print(run_times)

  print("Size\tTime(ns)\tCostant\t\tRatio")
  print(50*"-")
  for i in range(len(c_estimates)):
    print(f'{graphs_dimensions[i][0]}*log({graphs_dimensions[i][1]})', run_times[i], '', c_estimates[i], '', ratios[i], sep="\t")
  print(50*"-")

  # Plot

  c = 1000

  plot_complexity(c, graphs_dimensions, run_times, prim_asymptotic_behaviour)


if __name__ == "__main__":
  main()
