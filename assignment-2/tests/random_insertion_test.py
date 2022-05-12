import io
import unittest
from graph.graph import Graph, read_all
from tsp.tsp_file import TSPFileLabel
from algorithms.constructive_heuristics import random_insertion

class RandomInsertionTest(unittest.TestCase):
    def test_all_insertion(self):
        path = "tsp_dataset"
        A = read_all(path)
        #print(A)
        for i in range(len(A)): 
            g = A[i][0]
            n = int(g.get_information(TSPFileLabel.DIMENSION))
            current = random_insertion(g)
            current.sort()
            expected = [1] + list(range(1, n+1))

            #print(current)
            #print(expected)

            self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()