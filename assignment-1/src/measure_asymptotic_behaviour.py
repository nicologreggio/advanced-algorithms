from time import perf_counter_ns

def measure_run_time(alg, graph, num_calls):
  gc.disable()
  start_time = perf_counter_ns()
  
  for _ in range(num_calls):
    alg(graph)
  
  end_time = perf_counter_ns()
  gc.enable()
  avg_time = (end_time - start_time)/num_calls

  return avg_time


def map2(f1, f2, l, prepro = id):
  if not l: return ([], [])
  
  el = prepro(l[0])
  return tuple(x[0] + x[1] for x in zip(([f1(el)], [f2(el)]), map2(f1, f2, l[1:], prepro)))


def compute_asymptotic_constant(graphs, alg, asymptotic_behaviour, num_calls = 1000000):
  run_times, graphs_dimensions = map2(
    lambda graph:
      measure_run_time(alg, graph, num_calls),
    lambda graph:
      (graph.get_n(), graph.get_m()),
    graphs
  )

  ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(graphs) - 1)]

  c_estimates = [round(run_times[i]/asymptotic_behaviour(graph.get_m(), graph.get_n()),3) for i, graph in enumerate(graphs)]

  return (run_times, graphs_dimensions, ratios, c_estimates)
