from time import perf_counter_ns
import matplotlib.pyplot as plt
import gc
import copy

from algorithms.stoer_wagner import compute_cut_weight

# ANALYSIS FOR DETERMINISTIC ALGORITHM


def d_measure_run_time(alg, graph, num_calls):
    gc.disable()
    start_time = perf_counter_ns()

    for _ in range(num_calls):
        w = alg(graph)

    end_time = perf_counter_ns()
    gc.enable()
    avg_time = (end_time - start_time) / num_calls

    return w, avg_time


def d_compute_asymptotic_constant(graphs, alg, asymptotic_behaviour, num_calls=1000):
    run_times = []
    weights = []
    graphs_dimensions = []
    c_estimates = []
    ratios = [None]

    for graph in graphs:
        w, run_time = d_measure_run_time(alg, graph, num_calls)
        n = graph.get_n()
        m = graph.get_m()

        if run_times:
            ratios.append(round(run_time / run_times[-1], 3))

        run_times.append(run_time)
        weights.append(w)
        graphs_dimensions.append((n, m))
        c_estimates.append(round(run_time / asymptotic_behaviour(n, m), 3))

    return (run_times, graphs_dimensions, ratios, c_estimates, weights)


# ANALYSIS FOR RANDOMIZED ALGORITHM


def r_measure_run_time(alg, graph, num_calls):
    discovery_times = []
    gc.disable()
    start_time = perf_counter_ns()

    # return mincut and discovery time
    for _ in range(num_calls):
        min_cut_weight, discovery_time = alg(graph)
        discovery_times.append(discovery_time)

    end_time = perf_counter_ns()
    gc.enable()
    avg_time = (end_time - start_time) / num_calls
    avg_disc_time = sum(discovery_times) / num_calls

    return min_cut_weight, avg_time, avg_disc_time


def r_compute_asymptotic_constant(graphs, alg, asymptotic_behaviour, num_calls=1000):
    run_times = []
    discovery_times = []
    weights = []
    graphs_dimensions = []
    c_estimates = []
    ratios = [None]

    for graph in graphs:
        w, run_time, disc_time = r_measure_run_time(alg, graph, num_calls)
        n = graph.get_n()
        m = graph.get_m()

        if run_times:
            ratios.append(round(run_time / run_times[-1], 3))

        run_times.append(run_time)
        discovery_times.append(disc_time)
        weights.append(w)
        graphs_dimensions.append((n, m))
        c_estimates.append(round(run_time / asymptotic_behaviour(n, m), 3))

    return (run_times, discovery_times, graphs_dimensions, ratios, c_estimates, weights)


def plot_run_vs_discovery(
    run_times,
    discovery_times,
    graphs_dimensions,
    title,
):
    x = graphs_dimensions

    plt.plot(x, run_times, label="Runtimes")
    plt.plot(x, discovery_times, label="Discovery times")

    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.legend()
    plt.show()


# COMPLEXITY PLOT


def plot_complexity(
    C,
    run_times,
    graphs_dimensions,
    asymptotic_behaviour,
    title,
    expected_graphic_label,
    actual_graphic_label="Obtained complexity",
):
    x = [n for n, _ in graphs_dimensions]
    reference_z = [C * asymptotic_behaviour(n, m) for (n, m) in graphs_dimensions]

    plt.plot(x, reference_z, label=expected_graphic_label)
    plt.plot(x, run_times, label=actual_graphic_label)

    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.legend()
    plt.show()
