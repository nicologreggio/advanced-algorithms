import io
import unittest
from graph.graph import Graph, read_all
from tsp.tsp_file import TSPLabel
from algorithms.constructive_heuristics import random_insertion

class RandomInsertionTest(unittest.TestCase):
    def test_insertion(self):
        path = "/Users/dilettarigo/Desktop/advanced-algorithms/assignment-2/tsp_dataset"
        A = read_all(path)
        g = A[0][0]
        n = int(g.get_information(TSPLabel.DIMENSION))
        current = random_insertion(g)
        current.sort()
        expected = [1] + list(range(1, n+1))

        #print(current)
        #print(expected)

        self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()