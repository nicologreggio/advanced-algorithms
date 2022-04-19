import unittest

from src.union_find import UnionFind

class UnionFinderTest(unittest.TestCase):
  def test_init(self):
    data = list(range(10))
    uf = UnionFind(data)

    actual = uf.find(1)
    expected = 1

    self.assertEqual(expected, actual)

  
  def test_union(self):
    data = list(range(10))
    uf = UnionFind(data)
    
    uf.union(1, 2)
    uf.union(1, 3)
    uf.union(3, 4)

    uf.union(0, 1)
    uf.union(5, 6)
    uf.union(6, 3)
    uf.union(8, 6)
    uf.union(4, 8)

    actual = uf.find(8)
    expected = 1

    self.assertEqual(expected, actual)

  def test_multiple_union_same_element(self):
    data = list(range(10))
    uf = UnionFind(data)
    
    uf.union(1, 2)
    uf.union(1, 3)
    uf.union(3, 4)

    uf.union(0, 1)
    uf.union(5, 6)
    uf.union(6, 3)
    uf.union(8, 6)
    uf.union(4, 8)
    uf.union(4, 8)

    actual = uf.find(6)
    expected = 1

    self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
