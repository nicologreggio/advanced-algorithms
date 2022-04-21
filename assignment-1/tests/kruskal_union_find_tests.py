import io
import math
import unittest

from algorithms.kruskal_union_find import kruskal_union_find, kruskal_union_find_behaviour
from graph.graph import Graph, read_graph

class KruskalUnionFindTest(unittest.TestCase):
  def test_empty_graph(self):
    g = Graph()

    actual = kruskal_union_find(g)
    expected = []

    self.assertEqual(expected, actual)

  def test_tree_developed_right_child(self):
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

    actual = kruskal_union_find(g)
    expected = [
      (6, 7, -7462), (8, 9, -976), (4, 5, -433), (2, 3, 1392), (1, 2, 4993), (5, 6, 6590), (7, 8, 6658), (3, 4, 8856), (9, 10, 9698)
    ]

    self.assertEqual(expected, actual)

  def test_basic_graph_with_cycle(self):
    g = read_graph(io.StringIO(
    """10 12
      1 2 4993
      1 5 2432
      2 3 1392
      2 4 4687
      2 6 -34
      3 4 8856
      3 7 844
      3 8 -433
      5 9 -432
      6 9 -7462
      6 7 442
      8 10 -976"""))

    actual = kruskal_union_find(g)
    expected = [
      (6, 9, -7462), (8, 10, -976), (3, 8, -433), (5, 9, -432), (2, 6, -34), (6, 7, 442), (3, 7, 844), (1, 5, 2432), (2, 4, 4687)
    ]

    self.assertEqual(expected, actual)

  def test_full_connected_graph(self):
    g = read_graph(io.StringIO(
    """4 6
      1 2 -544
      1 3 455
      1 4 -12
      2 3 84
      2 4 27
      3 4 -7"""))

    actual = kruskal_union_find(g)
    expected = [
      (1, 2, -544), (1, 4, -12), (3, 4, -7)
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

    actual = kruskal_union_find_behaviour(g.get_n(), g.get_m())
    expected = g.get_m() * math.log(g.get_n())

    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
