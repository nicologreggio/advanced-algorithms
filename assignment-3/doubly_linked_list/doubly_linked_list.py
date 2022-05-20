from doubly_linked_list.doubly_linked_list_item import DoublyLinkedListItem
from doubly_linked_list.doubly_linked_list_iterator import DoublyLinkedListIterator


class DoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.size = 0

    def get_first_node(self):
        return self.first_node

    def append(self, x: DoublyLinkedListItem):
        if self.last_node:
            self.last_node.right = x
            x.left = self.last_node
        else:
            self.first_node = x

        self.last_node = x
        self.size += 1

    def remove(self, x: DoublyLinkedListItem):
        assert (self.size != 0, "Impossible to remove the element from an empty list")

        left = x.left
        right = x.right

        if left:
            left.right = right
        if right:
            right.left = left

        if x == self.last_node:
            self.last_node = left

        if x == self.first_node:
            self.first_node = right

        x.left = None
        x.right = None

        self.size -= 1

    def clean(self):
        self.first_node = None
        self.last_node = None
        self.size = 0

    def to_list(self):
        l = []
        for item in self:
            l.append(item)
        return l

    def __iter__(self):
        return DoublyLinkedListIterator(self.first_node)

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
