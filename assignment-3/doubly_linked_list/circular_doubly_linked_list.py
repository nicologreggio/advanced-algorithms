from doubly_linked_list.circular_doubly_linked_list_iterator import (
    CircularDoublyLinkedListIterator,
)


class DoublyLinkedListItem:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class CircularDoublyLinkedList:
    def __init__(self):
        self.nil = DoublyLinkedListItem()
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.size = 0

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

    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError(f"Impossible to get the element: {index} >= {self.size}")
        i = 0
        for item in self:
            if i == index:
                return item
            i += 1

    def __len__(self):
        return self.size

    def __str__(self):
        return f"{self.to_list()}"
