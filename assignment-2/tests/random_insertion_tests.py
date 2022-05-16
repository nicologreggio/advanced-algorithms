import unittest
from graph.graph import Graph, read_all
from tsp.tsp_file import TSPFileLabel
from algorithms.constructive_heuristics import random_insertion
from algorithms.measure_algorithm_performance import compute_approximate_solution
import math


class RandomInsertionTest(unittest.TestCase):
    def test_all_insertion(self):
        path = "tsp_dataset"
        A = read_all(path)
        for i in range(len(A)):
            g = A[i][0]
            n = int(g.get_information(TSPFileLabel.DIMENSION))
            current = random_insertion(g)
            current.sort()
            expected = [1] + list(range(1, n + 1))

            self.assertEqual(expected, current)

    def test_approx(self):
        path = "tsp_dataset"
        A = read_all(path)
        for i in range(len(A)):
            g = A[i][0]
            n = int(g.get_information(TSPFileLabel.DIMENSION))
            result = random_insertion(g)
            approximate_solution = compute_approximate_solution(g, result)
            optimal_solution = int(g.get_information(TSPFileLabel.OPTIMAL_SOLUTION))
            err = round((approximate_solution - optimal_solution) / optimal_solution, 4)
            assert err <= math.log(n) - 1


if __name__ == "__main__":
    unittest.main()
