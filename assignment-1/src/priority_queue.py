class PriorityQueue:
    def __init__(self):
        self.h = []
        self.indexes = {}
        self.size = 0 

    def min_heapify(self, i):
        if not self._is_leaf(i):
            if ((self.h[i] > self.h[self._left(i)]) or 
                (self._exist_right(i) and 
               self.h[i] > self.h[self._right(i)])):
 
                # Swap with the left child and heapify
                # the left child
                if self.h[self._left(i)] < self.h[self._right(i)]:
                    self._swap(i, self._left(i))
                    self.min_heapify(self._left(i))
 
                # Swap with the right child and heapify
                # the right child
                else:
                    self._swap(i, self._right(i))
                    self.min_heapify(self._right(i))

    def push(self, item):
        last_el = self.size
        self.h.append(item)
        
        self.size += 1
        self.indexes.update({item.get_value(): last_el})

        i = last_el
        p = self._parent(i)

        while i > 0 and self.h[i] < self.h[p]:
            self._swap(i, p)
            i = p
            p = self._parent(i)

    def pop(self):
        item = self.h[0]
        
        self.indexes.pop(item.get_value(), None)
        self.h[0] = self.h[self.size - 1]
        self.size -= 1

        i = 1
        while 2*i < self.size:
            l = self._left(i)
            r = self._right(i)

            if (2*i + 1) > self.size or self.h[l] < self.h[r]:
                if self.h[i] > self.h[l]:
                    self._swap(i, l)
                    i = l
                else:
                    break
            elif self.h[i] > self.h[r]:
                self._swap(i, r)
                i = r
            else:
                break



        return item

    def min_heap(self):
        for i in range(self.size//2, 0, -1):
            self.min_heapify(i)

    def get_index(self, v):
        return self.indexes.get(v, -1)

    def get_element(self, v):
        i = self.get_index(v)
        return self.get_element_by_index(i)

    def get_element_by_index(self, i):
        return self.h[i] if i >= 0 else None

    def get_element_and_index(self, v):
        i = self.get_index(v)
        return (i, self.get_element_by_index(i))

    def change_priority(self, v, new_key):
        i, el = self.get_element_and_index(v)
        el.change_key(new_key)

        p = self._parent(i)

        while i > 0 and self.h[i] < self.h[p]:
            self._swap(i, p)
            i = p
            p = self._parent(i)

    def _parent(self, i):
        return (i-1)//2

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return (2*i) + 2

    def _is_leaf(self, i):
        return i*2 > self._size

    def _exist_right(self, i):
        return self._right(i) < self._size

    def _swap(self, i, j):
        self.indexes[self.h[i].get_value()] = j
        self.indexes[self.h[j].get_value()] = i
        self.h[i], self.h[j] = self.h[j], self.h[i]

    def __len__(self):
        return self.size

    def __str__(self):
        return f'{self.h}'
