import math
from time import perf_counter_ns
from typing import Set, Tuple

from graph.graph import Graph, Vertex
from algorithms.stoer_wagner import compute_cut_weight


def karger_stein(g: Graph) -> Tuple[int, int]:
    k = math.ceil(math.log(g.get_n(), 2) ** 2)
    minimum = float("+inf")
    # minimum_cut = None

    start_time = perf_counter_ns()
    found_time = start_time
    for _ in range(k):
        w = g.recursive_contract()
        # C, w = g.recursive_contract() # wrong return type?
        # current_value = compute_cut_weight(g, *C)
        # TODO  w == current_value ???
        if w < minimum:
            minimum = w
            # minimum_cut = C
            found_time = perf_counter_ns()

        # if current_value < minimum:
        #    minimum = current_value
        #    minimum_cut = C
        #    found_time = perf_counter_ns()

    discovery_time = found_time - start_time
    # return minimum_cut, discovery_time
    return minimum, discovery_time


def karger_stein_asymptotic_behaviour(n: int, _) -> int:
    return n ** 2 * (math.log(n)) ** 3
