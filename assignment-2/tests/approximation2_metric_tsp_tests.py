import unittest
from graph.graph import Graph

from algorithms.approximation2_metric_tsp import (
    preorder_visit,
    approximation2_metric_tsp,
)


class Approximation2MetricTSPTest(unittest.TestCase):
    def test_preorder_visit_empty_graph(self):
        g = Graph()

        current = preorder_visit(g, r=1)
        expected = []

        self.assertEqual(expected, current)

    def test_preoder_visit(self):
        g = Graph(
            [
                (1, 3, 281),
                (1, 5, 291),
                (5, 6, 35),
                (6, 4, 70),
                (3, 8, 308),
                (8, 10, 180),
                (10, 9, 83),
                (3, 7, 611),
                (7, 2, 45),
            ]
        )

        current = preorder_visit(g, r=1)
        expected = [1, 3, 8, 10, 9, 7, 2, 5, 6, 4]

        self.assertEqual(expected, current)

    def test_approximation2_empty_graph(self):
        g = Graph()

        current = approximation2_metric_tsp(g)
        expected = []

        self.assertEqual(expected, current)

    def test_approximation2_small_graph(self):
        g = Graph(
            [
                (4, 5, 104),
                (1, 4, 396),
                (1, 3, 281),
                (4, 9, 611),
                (6, 8, 492),
                (9, 10, 83),
                (6, 10, 523),
                (1, 6, 326),
                (3, 10, 487),
                (3, 5, 509),
                (1, 10, 561),
                (8, 10, 180),
                (2, 6, 978),
                (5, 6, 35),
                (5, 9, 584),
                (1, 7, 641),
                (6, 7, 957),
                (5, 8, 471),
                (5, 7, 924),
                (7, 10, 1096),
                (1, 2, 666),
                (2, 3, 649),
                (4, 6, 70),
                (7, 8, 918),
                (3, 4, 604),
                (3, 6, 543),
                (4, 8, 525),
                (2, 8, 956),
                (2, 9, 1135),
                (6, 9, 596),
                (4, 10, 534),
                (3, 8, 308),
                (2, 5, 945),
                (2, 10, 1133),
                (8, 9, 183),
                (2, 7, 45),
                (2, 4, 1047),
                (5, 10, 513),
                (3, 7, 611),
                (4, 7, 1026),
                (7, 9, 1096),
                (1, 8, 427),
                (1, 9, 600),
                (1, 5, 291),
                (3, 9, 486),
            ]
        )

        current = approximation2_metric_tsp(g, r=1)
        expected = [1, 3, 8, 10, 9, 7, 2, 5, 6, 4, 1]

        self.assertEqual(expected, current)

    def test_approximation2_small_graph_dirrent_root(self):
        g = Graph(
            [
                (4, 5, 104),
                (1, 4, 396),
                (1, 3, 281),
                (4, 9, 611),
                (6, 8, 492),
                (9, 10, 83),
                (6, 10, 523),
                (1, 6, 326),
                (3, 10, 487),
                (3, 5, 509),
                (1, 10, 561),
                (8, 10, 180),
                (2, 6, 978),
                (5, 6, 35),
                (5, 9, 584),
                (1, 7, 641),
                (6, 7, 957),
                (5, 8, 471),
                (5, 7, 924),
                (7, 10, 1096),
                (1, 2, 666),
                (2, 3, 649),
                (4, 6, 70),
                (7, 8, 918),
                (3, 4, 604),
                (3, 6, 543),
                (4, 8, 525),
                (2, 8, 956),
                (2, 9, 1135),
                (6, 9, 596),
                (4, 10, 534),
                (3, 8, 308),
                (2, 5, 945),
                (2, 10, 1133),
                (8, 9, 183),
                (2, 7, 45),
                (2, 4, 1047),
                (5, 10, 513),
                (3, 7, 611),
                (4, 7, 1026),
                (7, 9, 1096),
                (1, 8, 427),
                (1, 9, 600),
                (1, 5, 291),
                (3, 9, 486),
            ]
        )

        current = approximation2_metric_tsp(g, r=6)
        expected = [6, 5, 1, 3, 8, 10, 9, 7, 2, 4, 6]

        self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()
