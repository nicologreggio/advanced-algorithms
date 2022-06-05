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

    def test_dict_insertion_order(self):
        h = {i: i*2 for i in range(0,100000)}
        l=list(h.values())
        rl=list(reversed(h.values()))

        for _ in range(500000):
            n=random.randrange(0,100000)
            self.assertEqual(h[n], l[n])
            self.assertNotEqual(h[n], rl[n])
    
    def test_weighted_degree_calculation(s):
        D=s.g.get_weighted_degree_list()
        s.assertEqual(5, len(s.g.get_vertices()))
        s.assertEqual(23, D[1])
        s.assertEqual(36, D[2])
        s.assertEqual(32, D[3])
        s.assertEqual(37, D[4])
        s.assertEqual(14, D[5])

        s.g.add_edge(1,2,3)
        s.assertEqual(26, D[1])
        s.assertEqual(39, D[2])

        s.g.remove_edge(4,5)
        s.assertEqual(34, D[4])
        s.assertEqual(11, D[5])

    
    def test_binary_search(self):
        # random.seed(42)
        # print([random.choice(range(1,100)) for _ in range(1,10)])
        C = [12, 31, 4, 95, 36, 32, 29, 18, 95]
        r1, r2, r3 = 70, 30, 100
        exp1, exp2, exp3 = 3, 1, None
        act1 = binary_search(C, r1)
        act2 = binary_search(C, r2)
        act3 = binary_search(C, r3)
        self.assertEqual(exp1, act1)
        self.assertEqual(exp2, act2)
        self.assertEqual(exp3, act3)

    def test_contract_edge(self):
        g = Graph([(1, 2, 4), (1, 3, 20), (2, 3, 3), (2, 3, 2)])
        D=g.get_weighted_degree_list()

        self.assertEqual(24, D[1])
        self.assertEqual(25, D[3])

        print(g.get_edges())
        g2 = g.contract_edge(1,2)

        Q=g2.get_weighted_degree_list()

        self.assertEqual(25, Q[1])
        self.assertEqual(25, Q[3])

        self.assertEqual(2, g2.get_m())
        print(g2.get_edges())

    def test_edge_select(self):
        g=self.g
        u,v=edge_select(g)
        self.assertIsNotNone(u)
        self.assertIsNotNone(v)

        print(f'selected edge: ({u},{v})')
        edges=set(map(lambda a: (a[0], a[1]), g.get_edges()))
        print(edges)
        
        # self.assertTrue((u,v) in edges) # not a proper way to check


if __name__ == "__main__":
    unittest.main()
