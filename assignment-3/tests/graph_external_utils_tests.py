import unittest
import random
from graph.graph import *


class GraphExternalUtilsTests(unittest.TestCase):
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

    def test_binary_search(self):
        # random.seed(42)
        # print([random.choice(range(1,100)) for _ in range(1,10)])
        C = [12, 31, 4, 95, 36, 32, 29, 18, 95]
        r1, r2, r3 = 70, 30, 100
        exp1, exp2, exp3 = 3, 1, None
        act1 = binary_search(self.g, C, r1)
        act2 = binary_search(self.g, C, r2)
        act3 = binary_search(self.g, C, r3)
        self.assertEqual(exp1, act1)
        self.assertEqual(exp2, act2)
        self.assertEqual(exp3, act3)

    def test_contract_edge(self):
        g = Graph([(1, 2, 4), (1, 3, 20), (2, 3, 3), (2, 3, 2)])
        D=g.get_weighted_degree_list()

        self.assertEqual(24, D[1])
        self.assertEqual(25, D[3])

        g2 = g.contract_edge(1,2)
        print(g2.get_edges())

        Q=g2.get_weighted_degree_list()

        self.assertEqual(25, Q[1])
        self.assertEqual(25, Q[3])

        self.assertEqual(4, g2.get_m())
        print(g2.get_edges())


if __name__ == "__main__":
    unittest.main()
