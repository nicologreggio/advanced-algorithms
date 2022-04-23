import argparse
from enum import Enum

from graph import graph
from graph.graph import Graph

from algorithms.measure_asymptotic_behaviour import compute_asymptotic_constant, plot_complexity

# Prim's algorithms
from algorithms.prim_priority_queue import prim_priority_queue, prim_priority_queue_asymptotic_behaviour
from algorithms.prim_sorted_set import prim_sorted_set, prim_sorted_set_asymptotic_behaviour

# Kruskal's algorithms
from algorithms.kruskal_union_find import kruskal_union_find, kruskal_union_find_asymptotic_behaviour
from algorithms.kruskal_naive import kruskal_naive, kruskal_naive_asymptotic_behaviour


def prim_priority_queue_complexity(graphs: list[Graph]):
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        prim_priority_queue,
        prim_priority_queue_asymptotic_behaviour,
        1000
    )

    print_complexity_data(
        run_times,
        graphs_dimensions,
        ratios,
        c_estimates,
        weight
    )

    C = sum(c_estimates) / len(c_estimates)

    plot_complexity(
        C,
        run_times,
        graphs_dimensions,
        prim_priority_queue_asymptotic_behaviour,
        "Prim's algorithm priority queue version",
        "Expected complexity: O(m*log(n))",
    )


def prim_sorted_set_complexity(graphs: list[Graph]):
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        prim_sorted_set,
        prim_sorted_set_asymptotic_behaviour,
        1000
    )

    print_complexity_data(
        run_times,
        graphs_dimensions,
        ratios,
        c_estimates,
        weight
    )

    C = sum(c_estimates) / len(c_estimates)

    plot_complexity(
        C,
        run_times,
        graphs_dimensions,
        prim_sorted_set_asymptotic_behaviour,
        "Prim's algorithm sorted set version",
        "Expected complexity: O(m*log(n))",
    )

def kruskal_naive_complexity(graphs: list[Graph]): 
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        kruskal_naive,
        kruskal_naive_asymptotic_behaviour,
        10
    )

    print_complexity_data(
        run_times,
        graphs_dimensions,
        ratios,
        c_estimates, 
        weight 
    )

    C = sum(c_estimates) / len(c_estimates)

    plot_complexity(
        C, 
        run_times, 
        graphs_dimensions, 
        kruskal_naive_asymptotic_behaviour,
        "Kruskal's algorithm naive version",
        "Expected complexity: O(m*n)",
    )


def kruskal_union_find_complexity(graphs: list[Graph]):
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        kruskal_union_find,
        kruskal_union_find_asymptotic_behaviour,
        100
    )

    print_complexity_data(
        run_times,
        graphs_dimensions,
        ratios,
        c_estimates,
        weight
    )

    C = sum(c_estimates) / len(c_estimates)

    plot_complexity(
        C, 
        run_times, 
        graphs_dimensions, 
        kruskal_union_find_asymptotic_behaviour,
        "Kruskal's algorithm union find version",
        "Expected complexity: O(m*log(n))",
    )

def print_complexity_data(run_times, graphs_dimensions, ratios, c_estimates, weight):
  print("Size\t\tTime(ns)\t\tConstant\t\tRatio\t\tWeight")
  print(90*"-")
  for i in range(len(c_estimates)):
      print(graphs_dimensions[i], run_times[i], '', c_estimates[i], '', ratios[i], '', weight[i], sep="\t")
  print(90*"-")


class MSTAlgorithms(Enum):
  all = 'all'
  prim_priority_queue = 'prim_priority_queue'
  prim_sorted_set = 'prim_sorted_set'
  kruskal_naive = 'kruskal_naive'
  kruskal_union_find = 'kruskal_union_find'
  def __str__(self):
      return self.value

def init_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", type=str, required=True)
  parser.add_argument(
      "--alg",
      type=MSTAlgorithms,
      choices=list(MSTAlgorithms),
      required=True)
      
  return parser


def main():
    args = init_args().parse_args()

    graphs = graph.read_all(args.d)[:28]

    algorithms = {
        MSTAlgorithms.prim_priority_queue: prim_priority_queue_complexity,
        MSTAlgorithms.prim_sorted_set: prim_sorted_set_complexity,
        MSTAlgorithms.kruskal_naive: kruskal_naive_complexity, 
        MSTAlgorithms.kruskal_union_find: kruskal_union_find_complexity,
    }

    if args.alg == MSTAlgorithms.all:
        for alg in list(algorithms.values()):
            alg(graphs)
    else:
        algorithms[args.alg](graphs)


if __name__ == "__main__":
    main()
    