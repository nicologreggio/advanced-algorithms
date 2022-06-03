import unittest
import random
from graph.graph import *

class GraphExternalUtilsTests(unittest.TestCase):
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

    def test_binary_search(self):
        # random.seed(42)
        # print([random.choice(range(1,100)) for _ in range(1,10)])
        C=[12, 31, 4, 95, 36, 32, 29, 18, 95]
        r1, r2, r3=70, 30, 100
        exp1, exp2, exp3=3, 1, None
        act1=binary_search(self.g, C, r1)
        act2=binary_search(self.g, C, r2)
        act3=binary_search(self.g, C, r3)
        self.assertEqual(exp1, act1)
        self.assertEqual(exp2, act2)
        self.assertEqual(exp3, act3)

if __name__ == "__main__":
    unittest.main()
