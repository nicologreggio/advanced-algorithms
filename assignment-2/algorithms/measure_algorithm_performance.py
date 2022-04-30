from time import perf_counter_ns
import gc


def measure_run_time(alg, graph, num_calls):
    gc.disable()
    start_time = perf_counter_ns()

    for _ in range(num_calls):
        approximate_solution = alg(graph)

    end_time = perf_counter_ns()
    gc.enable()
    avg_time = (end_time - start_time) / num_calls

    return avg_time, approximate_solution


def measure_algorithm_performance(alg, tsp_graphs, num_calls=100000):
    approximate_solutions = []
    run_times = []
    errors = []

    for graph, optimal_solution in tsp_graphs:
        run_time, approximate_solution = measure_run_time(alg, graph, num_calls)
        error = (approximate_solution - optimal_solution) / optimal_solution

        approximate_solutions.append(approximate_solution)
        run_times.append(run_time)
        errors.append(error)

    return (approximate_solutions, run_times, errors)
