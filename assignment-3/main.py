import argparse
from enum import Enum

#from graph import graph
#from graph.graph import Graph

from algorithms.analysis import (
    r_compute_asymptotic_constant,
    d_compute_asymptotic_constant,
    plot_complexity,
    plot_run_vs_discovery,
)

# from algorithms. +++ import +++

def error_function(approximate_solution, optimal_solution):
    return round((approximate_solution - optimal_solution) / optimal_solution, 4)

def stoer_wagner_complexity(graphs: "list[Graph]"):
    (run_times, 
    graphs_dimensions, 
    ratios, 
    c_estimates, 
    weights
    ) = d_compute_asymptotic_constant(graphs, stoer_wagner_algorithm, stoer_wagner_asymptotic_behaviour, 10)

    print("Stoer-Wagner algorithm")
    d_print_complexity_data(run_times, graphs_dimensions, ratios, c_estimates, weights)

    C = sum(c_estimates) / len(c_estimates)

    plot_complexity(
        C,
        run_times,
        graphs_dimensions,
        stoer_wagner_asymptotic_behaviour,
        "Stoer-Wagner deterministic algorithm"
        "Expected complexity: O(???)",
    )

def karger_stein_complexity(graphs: "list[Graph]"):
    (run_times, 
    discovery_times, 
    graphs_dimensions, 
    ratios, 
    c_estimates, 
    weights
    ) = r_compute_asymptotic_constant(graphs, karger_stein_algorithm, karger_stein_asymptotic_behaviour, 10)

    print("Karger-Stein algorithm")
    r_print_complexity_data(run_times, discovery_times, graphs_dimensions, ratios, c_estimates, weights)

    C = sum(c_estimates) / len(c_estimates)

    plot_complexity(
        C,
        run_times,
        graphs_dimensions,
        karger_stein_asymptotic_behaviour,
        "Karger-Stein randomized algorithm"
        "Expected complexity: O(n^2*log^3(n))",
    )

    plot_run_vs_discovery(run_times,
    discovery_times,
    graphs_dimensions,
    "Runtimes vs. Discovery Times for Karger-Stein algorithm",
    )

# TODO: add something to compute error 

def d_print_complexity_data(run_times, graphs_dimensions, ratios, c_estimates, weights):
    padding = len(str(max(run_times))) + 5
    headers = [
        str(h).ljust(padding)
        for h in ["Size", "Time(ns)", "Constant", "Ratio", "MinCut Weight"]
    ]
    hr = padding * (len(headers) + 2) * "-"
    print("\n\n\n")
    print(*headers, sep="\t")
    print(hr)
    for i in range(len(c_estimates)):
        print(
            str(graphs_dimensions[i]).ljust(padding),
            str(run_times[i]).ljust(padding),
            str(c_estimates[i]).ljust(padding),
            str(ratios[i]).ljust(padding),
            str(weights[i]).ljust(padding),
            sep="\t",
        )
    print(hr)

def r_print_complexity_data(run_times, discovery_times, graphs_dimensions, ratios, c_estimates, weights):
    padding = len(str(max(run_times))) + 5
    headers = [
        str(h).ljust(padding)
        for h in ["Size", "Time(ns)", "Discovery Time(ns)","Constant", "Ratio", "MinCut Weight"]
    ]
    hr = padding * (len(headers) + 2) * "-"
    print("\n\n\n")
    print(*headers, sep="\t")
    print(hr)
    for i in range(len(c_estimates)):
        print(
            str(graphs_dimensions[i]).ljust(padding),
            str(run_times[i]).ljust(padding),
            str(discovery_times[i]).ljust(padding),
            str(c_estimates[i]).ljust(padding),
            str(ratios[i]).ljust(padding),
            str(weights[i]).ljust(padding),
            sep="\t",
        )
    print(hr)


class MCAlgorithms(Enum):
    all = "all"
    stoer_wagner = "stoer_wagner"
    karger_stein = "karger_stein"

    def __str__(self):
        return self.value


def init_args():
    parser = argparse.ArgumentParser()

    def check_positive(v):
        v = int(v)
        if v <= 0:
            raise argparse.ArgumentTypeError(f"{v} is an invalid positive int value")
        return v

    parser.add_argument(
        "-d", "--directory", type=str, required=True, help="Path to the dataset to use"
    )
    parser.add_argument(
        "--alg",
        type=MCAlgorithms,
        choices=list(MCAlgorithms),
        required=True,
        help="Algorithm to execute on the chosen dataset among those available",
    )
    parser.add_argument(
        "--size",
        type=check_positive,
        help="How many dataset files to load",
    )
    parser.add_argument(
        "--calls",
        type=check_positive,
        help="How many times to run an algorithm",
        default=100,
    )

    return parser


def main():
    args = init_args().parse_args()

    mincut_graphs = graph.read_all(args.directory, args.size)

    algorithms = {
        MCAlgorithms.stoer_wagner: stoer_wagner_complexity,
        MCAlgorithms.karger_stein: karger_stein_complexity,
    }

    if args.alg == MCAlgorithms.all:
        for alg in algorithms.values():
            alg(mincut_graphs, args.calls)
    else:
        algorithms[args.alg](mincut_graphs, args.calls)


if __name__ == "__main__":
    main()
