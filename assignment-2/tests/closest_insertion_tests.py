import unittest
from graph.graph import Graph

from algorithms.constructive_heuristics import closest_insertion, closest_selection, get_dist


class ClosestInsertionTest(unittest.TestCase):
    def test_circuit_vertex_distance(self):
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

        C=[1,5,6,1]

        actual = get_dist(10, C, g)
        expected = 3

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
