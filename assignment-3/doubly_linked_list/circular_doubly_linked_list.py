from doubly_linked_list.doubly_linked_list import DoublyLinkedList, DoublyLinkedListItem
from doubly_linked_list.circular_doubly_linked_list_iterator import (
    CircularDoublyLinkedListIterator,
)


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.nil = DoublyLinkedListItem()
        self.nil.left = self.nil
        self.nil.right = self.nil

    def append(self, x: DoublyLinkedListItem):
        last_node = self.nil.left
        x.left = last_node
        x.right = self.nil

        last_node.right = x
        self.nil.left = x

        self.size += 1

    def remove(self, x: DoublyLinkedListItem):
        assert self.size != 0, "Impossible to remove the element from an empty list"

        x.left.right = x.right
        x.right.left = x.left

        x.left = None
        x.right = None

        self.size -= 1

    def clean(self):
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.size = 0

    def to_list(self):
        l = []
        for item in self:
            l.append(item)
        return l

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)

    def __str__(self):
        return self.to_list().__str__()
