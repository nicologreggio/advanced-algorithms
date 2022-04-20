from time import perf_counter_ns
import matplotlib.pyplot as plt
import gc


def measure_run_time(alg, graph, num_calls):
  gc.disable()
  start_time = perf_counter_ns()
  
  for _ in range(num_calls):
    mst = alg(graph)
  
  end_time = perf_counter_ns()
  gc.enable()
  avg_time = (end_time - start_time)/num_calls
  weight = sum([i[1] for i in mst])

  return avg_time, weight


# def map2(f1, f2, l):
#   if not l: return ([], [])
  
#   el = l[0]
#   return tuple(x[0] + x[1] for x in zip(([f1(el)], [f2(el)]), map2(f1, f2, l[1:])))


def compute_asymptotic_constant(graphs, alg, asymptotic_behaviour, num_calls = 1000000):
  run_times = []
  weight = []
  graphs_dimensions = []
  c_estimates = []

  for graph in graphs:
    run_time, w = measure_run_time(alg, graph, num_calls)

    n, m = graph.get_n(), graph.get_m()
    
    run_times.append(run_time)
    weight.append(w)
    graphs_dimensions.append((n, m))
    c_estimates.append(round(run_time/asymptotic_behaviour(n, m), 3))

  ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(graphs) - 1)]

  # c_estimates = [ for i, (n, m) in enumerate(graphs_dimensions)]
 
  return (run_times, graphs_dimensions, ratios, c_estimates, weight)


def plot_complexity(
  C, 
  run_times,
  graphs_dimensions, 
  asymptotic_behaviour,
  title,
  x_label,
  y_label = "Time",
  expected_graphic_label = 'Expected complexity',
  actual_graphic_label = 'Obtained complexity'
):
  x = [n*m for n, m in graphs_dimensions]
  reference_z = [C * asymptotic_behaviour(n, m) for n, m in graphs_dimensions]

  plt.plot(x, reference_z, label=expected_graphic_label)
  plt.plot(x, run_times, label=actual_graphic_label)
  
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.show()
