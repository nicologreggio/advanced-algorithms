from multiprocessing.dummy import active_children
from time import monotonic
import unittest
from graph.graph import Graph

from algorithms.constructive_heuristics import *

class MinTriangularTest(unittest.TestCase):
    def test_min_triangular(self):
        g=Graph(
            [
                (1, 2, 8),
                (1, 3, 6),
                (1, 4, 7),
                (1, 5, 2),
                (2, 3, 9),
                (2, 4, 15),
                (2, 5, 4),
                (3, 4, 12),
                (3, 5, 5),
                (4, 5, 3)
            ]
        )
        C=[1,4,5,1]
        actual=min_triangular(2, C, g)
        expected=3
        C.insert(actual, 2)
        
        self.assertEqual([1,4,5,2,1], C)
        self.assertEqual(expected, actual)