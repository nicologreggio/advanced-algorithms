from random import random
import unittest
from graph.graph import Graph
from algorithms.karger_stein import karger_stein, karger_stein_asymptotic_behaviour
import random


class KargerSteinTest(unittest.TestCase):
    def test_simple_karger_stein(self):
        random.seed(42)
        g = Graph([(1, 2, 4), (1, 3, 20), (2, 3, 3), (2, 3, 2)])
        print(g.get_weighted_degree_list())
        w, _ = karger_stein(g)

        self.assertEqual(w, 9)

    def test_bigger_karger_stein(self):
        random.seed(42)
        g = Graph(
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
                (4, 5, 3),
                (4, 6, 43),
                (5, 6, 23),
                (2, 7, 3),
            ]
        )
        print(g.get_weighted_degree_list())
        w, _ = karger_stein(g)

        self.assertEqual(w, 3)

    def test_karger_stein_asymptotic_behaviour(self):
        b=karger_stein_asymptotic_behaviour(5, 4)
        self.assertEqual(b, 104.2227891071413)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
