from doubly_linked_list.doubly_linked_list import DoublyLinkedList, DoublyLinkedListItem
from doubly_linked_list.linear_doubly_linked_list_iterator import (
    LinearDoublyLinkedListIterator,
)


class LinearDoublyLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.nil = DoublyLinkedListItem()
        self.last_node = self.nil

    def append(self, x: DoublyLinkedListItem):
        self.last_node.right = x
        x.left = self.last_node
        x.right = None

        self.last_node = x

        self.size += 1

    def remove(self, x: DoublyLinkedListItem):
        assert self.size != 0, "Impossible to remove the element from an empty list"

        right = x.right
        left = x.left

        if left:
            left.right = right
        if right:
            right.left = left

        x.right = None
        x.left = None

        self.size -= 1

    def clean(self):
        self.nil.left = None
        self.nil.right = None
        self.last_node = self.nil
        self.size = 0

    def to_list(self):
        l = []
        for item in self:
            l.append(item)
        return l

    def __iter__(self):
        return LinearDoublyLinkedListIterator(self)

    def __str__(self):
        return self.to_list().__str__()
