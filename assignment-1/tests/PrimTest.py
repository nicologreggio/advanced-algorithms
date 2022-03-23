import unittest
from io import StringIO

from src.filippo.prim import prim
from src.filippo.graph import Graph

class PrimTest(unittest.TestCase):
  def test_with_basic_graph(self):
    graph = StringIO("""10 9
1 2 4993
2 3 1392
3 4 8856
4 5 -433
5 6 6590
6 7 -7462
7 8 6658
8 9 -976
9 10 9698""")

    g = Graph.create_graph(graph)
    
    actual = prim(g)
    expected = [(0, 1, -1), (4993, 2, 1), (1392, 3, 2), (8856, 4, 3), (-433, 5, 4), (6590, 6, 5), (-7462, 7, 6), (6658, 8, 7), (-976, 9, 8), (9698, 10, 9)]

    self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
