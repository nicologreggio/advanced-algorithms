import io
import math
import unittest

from algorithms.kruskal_naive import is_acyclic, kruskal
from graph.graph import read_graph

class KruskalTest(unittest.TestCase):
  def test_is_acyclic_true(self):
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

    actual = is_acyclic(g)
    expected = True

    self.assertEqual(expected, actual)

  def test_is_acyclic_false(self):
    g = read_graph(io.StringIO(
    """10 9
      1 2 4993
      2 3 1392
      3 4 8856
      4 5 -433
      5 6 6590
      6 1 -7462
      6 8 6658
      8 9 -976
      9 10 9698"""))

    actual = is_acyclic(g)
    expected = False

    self.assertEqual(expected, actual)

  def test_kruskal_small_graph(self):
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
      9 10 9698"""
    ))

    actual_mst = kruskal(g)
    expected_mst = [(6, 7, -7462), (8, 9, -976), (4, 5, -433), (2, 3, 1392), (1, 2, 4993), (5, 6, 6590), (7, 8, 6658), (3, 4, 8856), (9, 10, 9698)]

    actual_size = len(actual_mst)
    expected_size = g.get_n() - 1

    self.assertEqual(expected_mst, actual_mst)
    self.assertEqual(expected_size, actual_size)


if __name__ == '__main__':
    unittest.main()
