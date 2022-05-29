from functools import total_ordering

from doubly_linked_list.circular_doubly_linked_list import (
    CircularDoublyLinkedList,
    DoublyLinkedListItem,
)


@total_ordering
class FibHeapItem(DoublyLinkedListItem):
    def __init__(self, name, key):
        super().__init__()
        self.name = name
        self.key = key
        self.mark = False
        self.parent = None
        self.children = CircularDoublyLinkedList()

    def get_degree(self):
        return len(self.children)

    def _reset_node(self):
        self.parent = None
        self.children.clean()

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.name == other.name and self.key == other.key

    def __str__(self):
        return f"({self.name}, {self.key}, {self.children})"

    def __repr__(self):
        return self.__str__()
