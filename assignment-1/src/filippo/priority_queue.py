class PriorityQueue:
    def __init__(self):
        self._h = []
        self._keys = {}
        self._size = 0 

    def min_heapify(self, i):

        if not self._is_leaf(i):
            if ((self._h[i] > self._h[self._left(i)]) or 
                (self._exist_right(i) and 
               self._h[i] > self._h[self._right(i)])):
 
                # Swap with the left child and heapify
                # the left child
                if self._h[self._left(i)] < self._h[self._right(i)]:
                    self._swap(i, self._left(i))
                    self.min_heapify(self._left(i))
 
                # Swap with the right child and heapify
                # the right child
                else:
                    self._swap(i, self._right(i))
                    self.min_heapify(self._right(i))

    def push(self, item):
        last_el = self._size
        self._size += 1
        
        self._h.append(item)
        self._keys.update({item.get_value(): last_el})

        i = last_el
        p = self._parent(i)

        while i > 0 and self._h[i] < self._h[p]:
            self._swap(i, p)
            i = p
            p = self._parent(i)

    def pop(self):
        item = self._h[0]
        
        self._keys.pop(item.get_value(), None)
        self._h[0] = self._h[self._size - 1]
        self._size -= 1

        i = 1

        while 2*i < self._size:
            l = self._left(i)
            r = self._right(i)

            if (2*i + 1) > self._size or self._h[l] < self._h[r]:
                if self._h[i] > self._h[l]:
                    self._swap(i, l)
                    i = l
                else:
                    break
            elif self._h[i] > self._h[r]:
                self._swap(i, r)
                i = r
            else:
                break



        return item

    def min_heap(self):
        for i in range(self._size//2, 0, -1):
            self.min_heapify(i)

    def get_index(self, v):
        return self._keys.get(v, -1)

    def get_element(self, v):
        i = self.get_index(v)
        return self.get_element_by_index(i)

    def get_element_by_index(self, i):
        return self._h[i] if i >= 0 else None

    def get_element_and_index(self, v):
        i = self.get_index(v)
        return (i, self.get_element_by_index(i))

    def change_priority(self, v, new_priority):
        i, el = self.get_element_and_index(v)
        el.priority = new_priority

        p = self._parent(i)

        while i > 0 and self._h[i] < self._h[p]:
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
        self._keys[self._h[i].get_value()] = j
        self._keys[self._h[j].get_value()] = i
        self._h[i], self._h[j] = self._h[j], self._h[i]

    def __len__(self):
        return self._size

    def __str__(self):
        return f'{self._h}'
