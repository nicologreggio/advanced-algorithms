import unittest
from graph.graph import Graph
from algorithms.stoer_wagner import st_min_cut, stoer_wagner


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
        expected = ((set([1, 3, 5, 6, 4, 8, 10, 7]), set([2])), 7, 2)

        self.assertEqual(expected, current)

    def test_st_mincut_complete_graph(self):
        g = Graph(
            [
                (1, 3, 281),
                (1, 3, 100),
                (1, 5, 291),
                (6, 5, 40),
                (5, 6, 35),
                (2, 1, 87),
                (6, 4, 70),
                (5, 4, 74),
                (3, 8, 308),
                (8, 10, 180),
                (10, 9, 83),
                (1, 9, 140),
                (3, 7, 611),
                (7, 2, 20),
                (7, 2, 45),
            ]
        )

        current = st_min_cut(g)
        expected = ((set([1, 2, 3, 5, 6, 7, 8, 9, 10]), set([4])), 6, 4)

        self.assertEqual(expected, current)

    def test_stoer_wagner(self):
        g = Graph(
            [
                (1, 3, 281),
                (1, 5, 291),
                (6, 4, 70),
                (3, 8, 19),
                (6, 8, 120),
                (8, 10, 180),
                (3, 7, 20),
                (7, 2, 45),
            ]
        )

        current = stoer_wagner(g)
        expected = (set([1, 8, 3, 5, 6, 4, 10, 7]), set([2]))

        self.assertEqual(expected, current)

    def test_stoer_wagner_complete_graph(self):
        g = Graph(
            [
                (1, 3, 281),
                (1, 3, 100),
                (1, 5, 291),
                (6, 5, 40),
                (5, 6, 35),
                (2, 1, 87),
                (6, 4, 70),
                (5, 4, 74),
                (3, 8, 308),
                (8, 10, 180),
                (10, 9, 83),
                (1, 9, 140),
                (3, 7, 611),
                (7, 2, 20),
                (7, 2, 45),
            ]
        )

        current = stoer_wagner(g)
        expected = (set([1, 2, 3, 5, 6, 7, 8, 9, 10]), set([4]))

        self.assertEqual(expected, current)

    def test_st_mincut_graph_with_same_weight(self):
        g = Graph([(1, 2, 1), (2, 3, 1), (3, 4, 1), (2, 4, 1)])

        current = st_min_cut(g)
        expected = ((set([1, 2, 4]), set([3])), 4, 3)

        self.assertEqual(expected, current)

    def test_stoer_wagner_graph_with_same_weight(self):
        g = Graph(
            [
                (1, 2, 1),
                (2, 3, 1),
                (3, 4, 1),
                (2, 4, 1),
            ]
        )

        current = stoer_wagner(g)
        expected = (set([2, 3, 4]), set([1]))

        self.assertEqual(expected, current)

    def test_st_mincut_complete_graph_with_same_weight(self):
        g = Graph(
            [
                (1, 2, 1),
                (2, 3, 1),
                (3, 4, 1),
                (4, 1, 1),
                (1, 3, 1),
                (2, 4, 1),
            ]
        )

        current = st_min_cut(g)
        expected = (({1, 2, 4}, {3}), 4, 3)

        self.assertEqual(expected, current)

    def test_stoer_wagner_complete_graph_with_same_weight(self):
        g = Graph(
            [
                (1, 2, 1),
                (2, 3, 1),
                (3, 4, 1),
                (4, 1, 1),
                (1, 3, 1),
                (2, 4, 1),
            ]
        )

        current = stoer_wagner(g)
        expected = (set([1, 3, 4]), set([2]))

        self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()
