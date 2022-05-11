import argparse
from enum import Enum
from graph import graph
from tsp.tsp_file import TSPFileLabel

from algorithms.measure_algorithm_performance import measure_algorithm_performance

from algorithms.approximation2_metric_tsp import approximation2_metric_tsp

# TODO: remove following 2 import when sure everything is fine
# from algorithms.closest_insertion import closest_insertion
# from algorithms.random_insertion import random_insertion
from algorithms.constructive_heuristics import closest_insertion, random_insertion


def error_function(approximate_solution, optimal_solution):
    return round((approximate_solution - optimal_solution) / optimal_solution, 4)


def measure_approximation2_algorithm(tsp_graphs, calls):
    approximate_solutions, run_times, errors = measure_algorithm_performance(
        approximation2_metric_tsp, tsp_graphs, error_function, calls
    )

    print("2-Approximation algorithm")
    print_measurement_data(tsp_graphs, approximate_solutions, run_times, errors)


def measure_closest_insertion(tsp_graphs, calls):
    approximate_solutions, run_times, errors = measure_algorithm_performance(
        closest_insertion, tsp_graphs, error_function, calls
    )

    print("Closest insertion algorithm")
    print_measurement_data(tsp_graphs, approximate_solutions, run_times, errors)


def measure_random_insertion_algorithm(tsp_graphs, calls):
    approximate_solutions, run_times, errors = measure_algorithm_performance(
        random_insertion, tsp_graphs, error_function, calls
    )

    print("Random insertion algorithm")
    print_measurement_data(tsp_graphs, approximate_solutions, run_times, errors)


def print_measurement_data(tsp_graphs, approximate_solutions, run_times, errors):
    padding = len(str(max(run_times))) + 5
    headers = [
        str(h).ljust(padding)
        for h in ["Name", "Approximate solution", "Time(ns)", "Error"]
    ]
    hr = padding * (len(headers) + 2) * "-"
    print(*headers, sep="\t")
    print(hr)
    for i in range(len(approximate_solutions)):
        g, _ = tsp_graphs[i]
        name = g.get_information(TSPFileLabel.NAME)
        print(
            str(name).ljust(padding),
            str(approximate_solutions[i]).ljust(padding),
            str(run_times[i]).ljust(padding),
            str(errors[i]).ljust(padding),
            sep="\t",
        )
    print(hr)


class TSPAlgorithms(Enum):
    all = "all"
    approximation2_metric_tsp = "approximation2_metric_tsp"
    closest_insertion = "closest_insertion"
    random_insertion = "random_insertion"

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
        type=TSPAlgorithms,
        choices=list(TSPAlgorithms),
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
        const=100,
        nargs="?",
    )

    return parser


def main():
    args = init_args().parse_args()

    tsp_graphs = graph.read_all(args.directory, args.size)

    algorithms = {
        TSPAlgorithms.approximation2_metric_tsp: measure_approximation2_algorithm,
        TSPAlgorithms.closest_insertion: measure_closest_insertion,
        TSPAlgorithms.random_insertion: measure_random_insertion_algorithm,
    }

    if args.alg == TSPAlgorithms.all:
        for alg in algorithms.values():
            alg(tsp_graphs, args.calls)
    else:
        algorithms[args.alg](tsp_graphs, args.calls)


if __name__ == "__main__":
    main()
