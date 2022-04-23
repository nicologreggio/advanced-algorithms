from functools import total_ordering


@total_ordering
class VertexHelper:
  def __init__(self, v, priority, parent):
    self.priority = priority
    self.v = v
    self.parent = parent

  def get_priority(self):
    return self.priority

  def get_value(self):
    return self.v

  def get_parent(self):
      return self.parent

  def set_parent(self, p):
    self.parent = p

  def change_priority(self, priority):
    self.priority = priority

  def __lt__(self, other):
    return self.priority < other.priority or (self.priority == other.priority and self.v < other.v)

  def __eq__(self, other):
    return self.priority == other.priority and self.v == other.v

  def __hash__(self):
    return hash(self.v)

  def __str__(self):
    return f'({self.v}, {self.priority}, {self.parent if self.parent else None})'

  def __repr__(self):
    return self.__str__()
