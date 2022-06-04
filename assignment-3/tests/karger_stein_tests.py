import unittest
from graph.graph import Graph
from algorithms.karger_stein import karger_stein

class KargerSteinTest(unittest.TestCase): 
    def test_dumb(self):
        g = Graph([(1, 2, 4), (1, 3, 20), (2, 3, 3), (2, 3, 2)])
        print(g.get_weighted_degree_list())
        w, _= karger_stein(g)
        
        self.assertEqual(w, 9)


"""if __name__ == "__main__":
    unittest.main()"""