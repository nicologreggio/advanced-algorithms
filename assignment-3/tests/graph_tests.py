import unittest
import random
from graph.graph import *
from graph.contraction import get_nth_vertex, contract


class GraphTests(unittest.TestCase):
    def __init__(self, sth) -> None:
        super().__init__(sth)
        self.g = Graph(
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
            ]
        )

    def test_get_nth_vertex(self):
        vertices = self.g.get_vertices()
        print(vertices)
        self.assertEqual(1, get_nth_vertex(vertices, 0))
        self.assertEqual(5, get_nth_vertex(vertices, 4))
        self.assertRaises(AssertionError, get_nth_vertex, vertices, 7)

    def test_weighted_degree_calculation(s):
        D = s.g.get_weighted_degree_list()
        s.assertEqual(5, len(s.g.get_vertices()))
        s.assertEqual(23, D[1])
        s.assertEqual(36, D[2])
        s.assertEqual(32, D[3])
        s.assertEqual(37, D[4])
        s.assertEqual(14, D[5])

        s.g.add_edge(1, 2, 3)
        s.assertEqual(26, D[1])
        s.assertEqual(39, D[2])

        s.g.remove_edge(4, 5)
        s.assertEqual(34, D[4])
        s.assertEqual(11, D[5])

    def test_contract(self):
        g = contract(self.g, 2)
        self.assertEqual(2, g.get_n())

    def test_repr(self):
        self.assertEqual("(V: 5, E: 10)", repr(self.g))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
