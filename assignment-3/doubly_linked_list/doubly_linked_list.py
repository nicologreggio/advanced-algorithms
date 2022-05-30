class DoublyLinkedListItem:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class DoublyLinkedList:
    def __init__(self):
        self.size = 0

    def append(self, x: DoublyLinkedListItem):
        pass

    def remove(self, x: DoublyLinkedListItem):
        pass

    def clean(self):
        pass

    def to_list(self):
        l = []
        for item in self:
            l.append(item)
        return l

    def __iter__(self):
        pass

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
