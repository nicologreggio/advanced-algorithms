class IPriorityQueueElement:
  def get_priority(self):
    pass
  
  def set_priority(self, priority):
    pass

  def get_name(self):
    pass


class PriorityQueue:
  def __init__(self):
    self.h = []
    self.indexes = {}
    self.size = 0

  def _parent(self, i: int) -> int:
    return (i - 1) // 2

  def _left(self, i: int) -> int:
    return 2*i + 1

  def _right(self, i: int) -> int:
    return 2*i + 2

  def _min_heapify(self, i: int):
    l = self._left(i)
    r = self._right(i)

    minimum = i

    if l < self.size and self.h[l] < self.h[minimum]:
      minimum = l

    if r < self.size and self.h[r] < self.h[minimum]:
      minimum = r
    
    if minimum != i:
      self._swap(minimum, i)
      self._min_heapify(minimum)

  def extract_min(self):
    minimum = self.h[0]
    maximum = self.h[self.size - 1]
    
    self.h[0] = maximum
    self.indexes.pop(minimum.get_name())
    self.indexes[maximum.get_name()] = 0
    self.size -= 1
    self._min_heapify(0)

    return minimum

  def insert(self, x: IPriorityQueueElement):
    priority = x.get_priority()
    x.set_priority(float("inf"))
    self.h.append(x)
    self.indexes[x.get_name()] = self.size
    self.size += 1

    self.decrease_key(self.size - 1, priority)  

  def decrease_key(self, i, new_priority):
    self.h[i].set_priority(new_priority)

    p = self._parent(i)
    while i > 0 and self.h[p] > self.h[i]:
      self._swap(i, p)
      i = p
      p = self._parent(i)

  def _swap(self, i: int, j: int):
    x = self.h[i]
    y = self.h[j]
    self.indexes[x.get_name()] = j
    self.indexes[y.get_name()] = i
    self.h[i], self.h[j] = y, x

  def get_index(self, x) -> int:
    return self.indexes.get(x, -1)

  def get_element(self, i: int):
    return self.h[i]

  def __len__(self) -> int:
    return self.size
