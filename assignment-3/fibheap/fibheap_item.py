from functools import total_ordering
from doubly_linked_list.doubly_linked_list import DoublyLinkedList, DoublyLinkedListItem


@total_ordering
class FibHeapItem(DoublyLinkedListItem):
    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key
        self.mark = False
        self._reset_node()

    def get_degree(self):
        return len(self.children)

    def _reset_node(self):
        self.parent = None
        self.children = DoublyLinkedList()

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.name == other.name and self.key == other.key

    def __str__(self):
        return f"({self.name}, {self.key})"

    def __repr__(self):
        return self.__str__()
