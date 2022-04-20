import argparse
from enum import Enum

from algorithms.measure_asymptotic_behaviour import compute_asymptotic_constant, plot_complexity
# from prim_smarter import prim, asymptotic_behaviour as prim_behaviour
from algorithms.prim import prim, asymptotic_behaviour as prim_behaviour
from algorithms.kruskal_union_find import kruskal_union_find, kruskal_union_find_behaviour
from algorithms.kruskal_naive import kruskal, kruskal_behaviour
from graph import graph

def prim_complexity(graphs):
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        prim,
        prim_behaviour,
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
        prim_behaviour,
        "Prim's algorithm",
        "m*log(n)"
    )

def kruskal_naive_complexity(graphs): 
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        kruskal,
        kruskal_behaviour,
        1000
    )

    print_complexity_data(
        run_times,
        graphs_dimensions,
        ratios,
        c_estimates, 
        weight 
    )

    C = min(c_estimates)

    plot_complexity(
        C, 
        run_times, 
        graphs_dimensions, 
        kruskal_behaviour,
        "Kruskal's algorithm naive version",
        "m*n"
    )


def kruskal_union_find_complexity(graphs):
    run_times, graphs_dimensions, ratios, c_estimates, weight = compute_asymptotic_constant(
        graphs,
        kruskal_union_find,
        kruskal_union_find_behaviour,
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
    # C = 300

    plot_complexity(
        C, 
        run_times, 
        graphs_dimensions, 
        kruskal_union_find_behaviour,
        "Kruskal's algorithm union find version",
        "m*log(n)"
    )

def print_complexity_data(run_times, graphs_dimensions, ratios, c_estimates, weight):
  print("Size\t\tTime(ns)\t\tCostant\t\tRatio\t\tWeight")
  print(90*"-")
  for i in range(len(c_estimates)):
      print(f'{graphs_dimensions[i]}', run_times[i], '', c_estimates[i], '', ratios[i], '', weight[i], sep="\t")
  print(90*"-")


class MSTAlgorithms(Enum):
  all = 'all'
  prim = 'prim'
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

    graphs = graph.read_all(args.d)

    algorithms = {
        MSTAlgorithms.prim: prim_complexity,
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
    