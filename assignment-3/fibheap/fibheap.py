import math
from fibheap.fibheap_item import FibHeapItem
from doubly_linked_list.doubly_linked_list import DoublyLinkedList


class FibHeap:
    def __init__(self):
        self.roots = DoublyLinkedList()
        self.max = None
        self.size = 0

    def insert(self, x: FibHeapItem):
        x._reset_node()
        self.roots.append(x)

        if not self.max or self.max < x:
            self.max = x

        self.size += 1

    def maximum(self):
        return self.max

    def extract_maximum(self):
        z = self.max

        if z:
            for child in z.children:
                self.roots.append(child)
                child.parent = None

            self.roots.remove(z)

            if id(z) == id(z.right):
                self.max = None
            else:
                self.max = z.right
                self._consolidate()

            self.size -= 1

        return z

    def increase_key(self, x: FibHeapItem, key):
        assert (key > x.key, "The new key is less or equal than the old one")

        x.key = key
        y = x.parent
        if y and x > y:
            self._cut(x, y)
            self._cascading_cut(y)

        if x > self.max:
            self.max = x

    def _cut(self, x: FibHeapItem, y: FibHeapItem):
        y.children.remove(x)
        self.roots.append(x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, x: FibHeapItem):
        z = x.p
        if not z:
            if x.mark == False:
                x.mark = True
            else:
                self._cut(x, z)
                self._cascading_cut(z)

    def _consolidate(self):
        max_degree = self._compute_max_degree()
        A = [None] * max_degree

        for x in self.roots:
            d = x.get_degree()
            while A[d]:
                y = A[d]
                if x < y:
                    x, y = y, x
                self._fib_heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x

        self.max = None

        for i in range(max_degree):
            el = A[i]
            if el:
                if not self.max:
                    self.roots.clean()
                    self.roots.append(el)
                    self.max = el
                else:
                    self.roots.append(el)
                    if el > self.max:
                        self.max = el

    def _fib_heap_link(self, y: FibHeapItem, x: FibHeapItem):
        self.roots.remove(y)
        y.parent = x
        x.children.append(y)

        y.mark = False

    def _compute_max_degree(self):
        FI = 1.61803
        return math.floor(math.log(self.size, FI))

    def __len__(self):
        return self.size