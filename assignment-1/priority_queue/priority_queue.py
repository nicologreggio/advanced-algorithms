class PriorityQueue:
  def __init__(self):
    self.h = []
    self.indexes = {}
    self.size = 0

  def parent(self, i):
    return (i - 1) // 2

  def left(self, i):
    return 2*i + 1

  def right(self, i):
    return 2*i + 2

  def min_heapify(self, i):
    l = self.left(i)
    r = self.right(i)

    minimum = i

    if l < self.size and self.h[l] < self.h[minimum]:
      minimum = l

    if r < self.size and self.h[r] < self.h[minimum]:
      minimum = r
    
    if minimum != i:
      self.swap(minimum, i)
      self.min_heapify(minimum)

  def extract_min(self):
    minimum = self.h[0]
    maximum = self.h[self.size - 1]
    
    self.h[0] = maximum
    self.indexes.pop(minimum.get_value())
    self.indexes[maximum.get_value()] = 0
    self.size -= 1
    self.min_heapify(0)

    return minimum

  def insert(self, x):
    priority = x.get_priority()
    x.change_priority(float("inf"))
    self.h.append(x)
    self.indexes[x.get_value()] = self.size
    self.size += 1

    self.decrease_key(self.size - 1, priority)  

  def decrease_key(self, i, new_priority):
    self.h[i].change_priority(new_priority)

    p = self.parent(i)
    while i > 0 and self.h[p] > self.h[i]:
      self.swap(i, p)
      i = p
      p = self.parent(i)

  def swap(self, i, j):
    x = self.h[i]
    y = self.h[j]
    self.indexes[x.get_value()] = j
    self.indexes[y.get_value()] = i
    self.h[i], self.h[j] = y, x

  def get_index(self, x):
    return self.indexes.get(x, -1)

  def get_element(self, i):
    return self.h[i]

  def __len__(self):
    return self.size
