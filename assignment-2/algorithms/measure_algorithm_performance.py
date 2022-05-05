from graph.graph import Graph, Vertex
from time import perf_counter_ns
import gc


def compute_approximate_solution(g: Graph, H: "list[Vertex]"):
    approximate_solution = 0
    last_vertex = H[0]

    for v in H[1:]:
        approximate_solution += g.get_weight(last_vertex, v)
        last_vertex = v

    return approximate_solution


def measure_run_time(alg, graph, num_calls):
    gc.disable()
    start_time = perf_counter_ns()

    for _ in range(num_calls):
        H = alg(graph)

    end_time = perf_counter_ns()
    gc.enable()
    avg_time = (end_time - start_time) / num_calls

    # approximate_solution = sum([e[2] for e in H])
    approximate_solution = compute_approximate_solution(graph, H)

    return avg_time, approximate_solution


def measure_algorithm_performance(alg, tsp_graphs, error_function, num_calls=100000):
    approximate_solutions = []
    run_times = []
    errors = []

    for graph, optimal_solution in tsp_graphs:
        run_time, approximate_solution = measure_run_time(alg, graph, num_calls)
        error = error_function(approximate_solution, optimal_solution)

        approximate_solutions.append(approximate_solution)
        run_times.append(run_time)
        errors.append(error)

    return (approximate_solutions, run_times, errors)
