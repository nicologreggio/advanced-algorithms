class LinearDoublyLinkedListIterator:
    def __init__(self, l):
        self.l = l
        self.node = l.nil.right

    def __iter__(self):
        return self

    def __next__(self):
        if not self.node:
            raise StopIteration()

        tmp = self.node

        self.node = self.node.right

        return tmp
