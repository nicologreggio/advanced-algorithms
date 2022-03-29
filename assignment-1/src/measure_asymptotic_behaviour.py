from time import perf_counter_ns
import matplotlib.pyplot as plt
import gc


def measure_run_time(alg, graph, num_calls):
  gc.disable()
  start_time = perf_counter_ns()
  
  for _ in range(num_calls):
    alg(graph)
  
  end_time = perf_counter_ns()
  gc.enable()
  avg_time = (end_time - start_time)/num_calls

  return avg_time


def map2(f1, f2, l):
  if not l: return ([], [])
  
  el = l[0]
  return tuple(x[0] + x[1] for x in zip(([f1(el)], [f2(el)]), map2(f1, f2, l[1:])))


def compute_asymptotic_constant(graphs, alg, asymptotic_behaviour, num_calls = 1000000):
  run_times, graphs_dimensions = map2(
    lambda graph: measure_run_time(alg, graph, num_calls),
    lambda graph: (graph.get_n(), graph.get_m()),
    graphs
  )

  ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(graphs) - 1)]

  c_estimates = [round(run_times[i]/asymptotic_behaviour(graph.get_m(), graph.get_n()),3) for i, graph in enumerate(graphs)]

  return (run_times, graphs_dimensions, ratios, c_estimates)


def plot_complexity(C, run_times, graphs_dimensions, asymptotic_behaviour):
  x = [n*m for n, m in graphs_dimensions]
  reference_z = [C * asymptotic_behaviour(n, m) for n, m in graphs_dimensions]

  plt.plot(x, reference_z, 'C1', label='C1')
  plt.plot(x, run_times, 'C2', label='C2')
  plt.legend()
  plt.show()
