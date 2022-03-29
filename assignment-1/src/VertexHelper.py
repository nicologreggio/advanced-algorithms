class VertexHelper:
  def __init__(self, key, v, parent):
    self.key = key
    self.v = v
    self.parent = parent

  def get_key(self):
    return self.key

  def get_value(self):
    return self.v

  def set_parent(self, p):
    self.parent = p

  def change_key(self, key):
    self.key = key

  def __lt__(self, other):
      return self.key < other.key

  def __str__(self):
    return f'({self.key}, {self.v}, {self.parent.get_value() if self.parent else None})'

  def __repr__(self):
    return self.__str__()
    