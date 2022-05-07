import argparse
from enum import Enum
from graph import graph

from algorithms.measure_algorithm_performance import measure_algorithm_performance

from algorithms.approximation2_metric_tsp import approximation2_metric_tsp
from algorithms.closest_insertion import closest_insertion


def error_function(approximate_solution, optimal_solution):
    return (approximate_solution - optimal_solution) / optimal_solution


def measure_approximation2_algorithm(tsp_graphs):
    approximate_solutions, run_times, errors = measure_algorithm_performance(
        approximation2_metric_tsp, tsp_graphs, error_function, 1
    )

    print_measurement_data(approximate_solutions, run_times, errors)

def measure_closest_insertion(tsp_graphs):
    approximate_solutions, run_times, errors = measure_algorithm_performance(
        closest_insertion, tsp_graphs, error_function, 1
    )

    print_measurement_data(approximate_solutions, run_times, errors)


def print_measurement_data(approximate_solutions, run_times, errors):
    padding = len(str(max(run_times))) + 5
    headers = [
        str(h).ljust(padding) for h in ["Approximate solution", "Time(ns)", "Error"]
    ]
    hr = padding * (len(headers) + 2) * "-"
    print(*headers, sep="\t")
    print(hr)
    for i in range(len(approximate_solutions)):
        print(
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

    return parser


def main():
    args = init_args().parse_args()

    tsp_graphs = graph.read_all(args.directory, args.size)

    algorithms = {
        TSPAlgorithms.approximation2_metric_tsp: measure_approximation2_algorithm,
        TSPAlgorithms.closest_insertion: measure_closest_insertion
    }

    if args.alg == TSPAlgorithms.all:
        for alg in algorithms.values():
            alg(tsp_graphs)
    else:
        algorithms[args.alg](tsp_graphs)


if __name__ == "__main__":
    main()
