import io
import math
import unittest

from algorithms.kruskal_smart import kruskal_smart, kruskal_smart_behaviour
from graph.graph import Graph, read_graph

class KruskalSmartTest(unittest.TestCase):
  def test_empty_graph(self):
    g = Graph()

    actual = kruskal_smart(g)
    expected = []

    self.assertEqual(expected, actual)

  def test_basic_graph(self):
    g = read_graph(io.StringIO(
    """10 9
      1 2 4993
      2 3 1392
      3 4 8856
      4 5 -433
      5 6 6590
      6 7 -7462
      7 8 6658
      8 9 -976
      9 10 9698"""))

    actual = kruskal_smart(g)
    expected = [
      ((6, 7), -7462), ((8, 9), -976), ((4, 5), -433), ((2, 3), 1392), ((1, 2), 4993), ((5, 6), 6590), ((7, 8), 6658), ((3, 4), 8856), ((9, 10), 9698)
    ]

    self.assertEqual(expected, actual)


  def test_complexity_behaviour(self):
    g = read_graph(io.StringIO(
    """10 9
      1 2 4993
      2 3 1392
      3 4 8856
      4 5 -433
      5 6 6590
      6 7 -7462
      7 8 6658
      8 9 -976
      9 10 9698"""))

    actual = kruskal_smart_behaviour(g.get_n(), g.get_m())
    expected = g.get_m() * math.log(g.get_n())

    self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()
