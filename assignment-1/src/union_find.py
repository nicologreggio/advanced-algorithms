class UnionFind:
  def __init__(self, n):
    self.data = list(range(n))
    self.sizes = {}

    for el in self.data:
      self.sizes.update({el: 0})

  def find(self, el):
    if el == self._parent(el): return el

    return self.find(self._parent(el))

  def union(self, x, y):
    i = self.find(x)
    j = self.find(y)

    if i != j:
      if self.sizes[i] >= self.sizes[j]:
        self._change_parent(j, i)
      else:
        self._change_parent(i, j)

  def _change_parent(self, i, new_parent):
    self.sizes[self.data[i]] -= 1
    self.sizes[new_parent] += 1

    self.data[i] = new_parent

  def _parent(self, i):
    return self.data[i]

  def __eq__(self, o):
      return self.data == o.data

  def __str__(self):
    return self.data
    