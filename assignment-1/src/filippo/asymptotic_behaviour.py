from cProfile import run
from functools import reduce
import gc
import functools

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


# def measure_run_time(alg, graphs, num_calls):
#   sum_times = 0.0

#   print("I'm computing...")

#   for graph in graphs:
#     gc.disable()
#     start_time = perf_counter_ns()
#     for _ in range(num_calls):
#       alg(graph)
#     end_time = perf_counter_ns()
#     gc.enable()
#     sum_times += (end_time - start_time)/num_calls

#   print("Done\n")
  
#   avg_time = int(round(sum_times/len(graphs)))
#   # return average time in nanoseconds
#   return avg_time


def compute_asymptotic_constant(alg, asymptotic_behaviour, graphs, num_calls):
  run_times = [measure_run_time(alg, graph, num_calls) for graph in graphs]

  ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(graphs) - 1)]

  c_estimates = [round(run_times[i]/asymptotic_behaviour(graph.get_m(), graph.get_n()),3) for i, graph in enumerate(graphs)]

  return (run_times, ratios, c_estimates)
  

def map2(l, f1, f2, prepro = id):
  if not l: return ([], [])
  
  el = prepro(l[0])
  return tuple(x[0] + x[1] for x in zip(([f1(el)], [f2(el)]), map2(l[1:], f1, f2, prepro)))

def compute_asymptotic_constant_light(alg, asymptotic_behaviour, files, init_graph_function, num_calls = 100000):
  run_times, graphs_dimensions = map2(
    files,
    lambda graph:
      measure_run_time(alg, graph, num_calls),
    lambda graph:
      (graph.get_n(), graph.get_m()),
    init_graph_function
  )

  print(graphs_dimensions)

  ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(run_times) - 1)]

  c_estimates = [round(run_times[i]/asymptotic_behaviour(n, m),3) for i, (n, m) in enumerate(graphs_dimensions)]

  return (graphs_dimensions, run_times, ratios, c_estimates)
  

# def compute_asymptotic_constant(alg, asymptotic_behaviour, grouped_graphs, num_calls):
#   run_times = [measure_run_time(alg, graphs, num_calls) for graphs in grouped_graphs]

#   ratios = [None] + [round(run_times[i+1]/run_times[i],3) for i in range(len(grouped_graphs) - 1)]

#   def sum_asymptotic_behaviour(graphs):
#     return functools.reduce(
#       lambda acc, graph: 
#         acc + asymptotic_behaviour(graph.get_m(), graph.get_n()), 
#       graphs, 
#       0
#     )

#   c_estimates = [round(run_times[i]/sum_asymptotic_behaviour(graphs),3) for i, graphs in enumerate(grouped_graphs)]

#   return (run_times, ratios, c_estimates)

