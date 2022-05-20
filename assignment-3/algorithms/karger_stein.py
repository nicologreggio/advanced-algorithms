import math
from time import perf_counter_ns


def karger_stein(g):
    k = math.log(g.get_n()) ** 2
    minimum = float("-inf")

    start_time = perf_counter_ns()
    found_time = start_time
    for i in range(k):
        t = g.recursive_contract()
        if t < minimum:
            minimum = t
            found_time = perf_counter_ns()

    discovery_time = found_time - start_time
    return minimum, discovery_time


def karger_stein_asymptotic_behaviour(n, _):
    return n ** 2 * (math.log(n)) ** 3
