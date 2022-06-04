import unittest
from graph.graph import Graph
from algorithms.karger_stein import karger_stein

class KargerSteinTest(unittest.TestCase): 

    def simple_test(self):
        g = Graph([(1, 2, 4), (1, 3, 20), (2, 3, 3), (2, 3, 2)])
        C, w = karger_stein(g)
        
        self.assertEqual(C, (set(1, 3), set(2)))
        self.assertEqual(w, 9)


if __name__ == "__main__":
    unittest.main()