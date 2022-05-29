import unittest
from graph.graph import Graph
from algorithms.stoer_wagner import st_min_cut


class StoerWagnerTest(unittest.TestCase):
    def test_st_mincut(self):
        g = Graph(
            [
                (1, 3, 281),
                (1, 5, 291),
                (6, 4, 70),
                (3, 8, 308),
                (6, 8, 20),
                (8, 10, 180),
                (3, 7, 20),
                (7, 2, 45),
            ]
        )

        current = st_min_cut(g)
        expected = ((set([1, 3, 5, 6, 4, 8, 10, 7]), set([2])), 2, 7)

        self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()
