import unittest
from graph.graph import Graph

from algorithms.constructive_heuristics import closest_insertion, closest_selection, get_dist


class ClosestInsertionTest(unittest.TestCase):
    def __init__(self, sth) -> None:
        super().__init__(sth)
        self.g=Graph(
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

    def test_circuit_vertex_distance(self):
        C=[2,4,5,2]

        actual = get_dist(1, C, self.g)
        expected = 2

        self.assertEqual(expected, actual)

    def test_closest_selection(self):
        C=[1,5,1]
        k=closest_selection(C, set(self.g.get_vertices()), self.g)

        expected=4
        self.assertEqual(expected, k)
        
    def test_closest_insertion(self):
        expected=[1,4,5,2,3,1]
        actual=closest_insertion(self.g)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
