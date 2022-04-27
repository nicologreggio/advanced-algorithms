import argparse
from enum import Enum
from graph import graph


class TSPAlgorithms(Enum):
    all = "all"

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
        help="How many files of the dataset load",
    )

    return parser


def main():
    args = init_args().parse_args()

    graphs = graph.read_all(args.directory, args.size)

    algorithms = {}

    if args.alg == TSPAlgorithms.all:
        for alg in algorithms.values():
            alg(graphs)
    else:
        algorithms[args.alg](graphs)


if __name__ == "__main__":
    main()
