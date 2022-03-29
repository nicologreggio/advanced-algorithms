import argparse
from enum import Enum
from measure_asymptotic_behaviour import compute_asymptotic_constant, plot_complexity
# from prim_smarter import prim, asymptotic_behaviour as prim_behaviour 
from prim import prim, asymptotic_behaviour as prim_behaviour 
import graph

select_complexity_constant_function = lambda x: sum(x) / len(x)

def prim_complexity(graphs):
  run_times, graphs_dimensions, ratios, c_estimates = compute_asymptotic_constant(
    graphs,
    prim,
    prim_behaviour,
    10
  )

  print_complexity_data(run_times, graphs_dimensions, ratios, c_estimates)

  C = select_complexity_constant_function(c_estimates)

  plot_complexity(C, run_times, graphs_dimensions, prim_behaviour)
  

def print_complexity_data(run_times, graphs_dimensions, ratios, c_estimates):
  print(run_times)
  print(c_estimates)

  print("Size\t\tTime(ns)\t\tCostant\t\tRatio")
  print(90*"-")
  for i in range(len(c_estimates)):
    print(f'{graphs_dimensions[i][0]}*log({graphs_dimensions[i][1]})', run_times[i], '', c_estimates[i], '', ratios[i], sep="\t")
  print(90*"-")


class MSTAlgorithms(Enum):
    all = 'all'
    prim = 'prim'
    kruskal_stupid = 'kruskal_stupid'
    kruskal_smart = 'kruskal_smart'

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
        MSTAlgorithms.prim: prim_complexity
    }

    if args.alg == MSTAlgorithms.all:
      for alg in list(algorithms.values()):
        alg(graphs)
    else:
      algorithms[args.alg](graphs)

if __name__ == "__main__":
    main()
