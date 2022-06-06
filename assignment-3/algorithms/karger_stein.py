import math
from time import perf_counter_ns
from typing import Tuple
from graph.graph import Graph


def karger_stein(g: Graph) -> Tuple[int, int]:
    print("Running on ", g)
    k = math.ceil(math.log(g.get_n(), 2) ** 2)
    minimum = float("+inf")

    start_time = perf_counter_ns()
    found_time = start_time
    for _ in range(k):
        w = g.recursive_contract()

        if w < minimum:
            minimum = w
            found_time = perf_counter_ns()

    discovery_time = found_time - start_time

    return minimum, discovery_time


def karger_stein_asymptotic_behaviour(n: int, _) -> int:
    return n ** 2 * (math.log(n)) ** 3
