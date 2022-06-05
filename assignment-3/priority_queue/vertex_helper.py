from functools import total_ordering
from priority_queue.priority_queue import IPriorityQueueElement


@total_ordering
class VertexHelper(IPriorityQueueElement):
    def __init__(self, name, priority, parent=None):
        self.priority = priority
        self.name = name
        self.parent = parent

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority and self.name == other.name

    def __str__(self):
        return f"({self.name}, {self.priority}, {self.parent if self.parent else None})"

    def __repr__(self):
        return self.__str__()
