class PriorityQueue:
    def __init__(self):
        self.h = []
        self.indexes = {}
        self.size = 0 

    def min_heapify(self, i):
        l = self._left(i)
        r = self._right(i)

        minimum = i

        if l < self.size and self.h[l] < self.h[i]:
            minimum = l
        
        if r < self.size and self.h[r] < self.h[i]:
            minimum = r

        if minimum != i:
            self._swap(minimum, i)
            self.min_heapify(minimum)

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

        self.indexes[self.h[0].get_value()] = 0

        # i = 0
        # while 2*i < self.size:
        #     l = self._left(i)
        #     r = self._right(i)

        #     if (2*i + 1) > self.size or self.h[l] < self.h[r]:
        #         if self.h[i] > self.h[l]:
        #             self._swap(i, l)
        #             i = l
        #         else:
        #             break
        #     elif self.h[i] > self.h[r]:
        #         self._swap(i, r)
        #         i = r
        #     else:
        #         break

        self.min_heapify(0)

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

    def change_priority(self, v, new_priority):
        i, el = self.get_element_and_index(v)
        el.change_priority(new_priority)

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



'''
class PriorityQueue: 
    def __init__(self): 
        self.list = []
        self.index = {}
        self.size = 0

    def __repr__(self): 
        return "{0}".format(self.list)
        
    def parent(self, i): 
        return (i - 1)// 2 
    
    def left(self, i): 
        return 2*i +1

    def right(self, i): 
        return (2*i) +2

    def swap(self, i, j): 
        self.index[self.list[i].name] = j 
        self.index[self.list[j].name] = i
        self.list[i], self.list[j] = self.list[j], self.list[i]

    def min_heapify(self, i): 
        l = self.left(i)
        r = self.right(i)
        if (l < self.size) and (self.list[l] < self.list[i]): 
            min = l 
        else: 
            min = i 
        if (r < self.size) and (self.list[r] < self.list[min]): 
            min = r 
        if min != i: 
            self.swap(i, min)
            self.min_heapify(min)

    def build_min_heap(self): 
        for i in reversed(range((self.size//2)+1)): 
            self.min_heapify(i)

    # problem here in the size!
    def extract_min(self): 
        min = self.list[0]
        self.index.pop(min.name)
        v = self.list[self.size-1]
        self.list[0] = v
        self.index[v.namez] = 0
        # self.list.pop()
        self.size -= 1
        self.min_heapify(0)

        print(self.index)

        return min

    def min_heapify_up(self, i): 
        p = self.parent(i)
        if (i > 0 and self.list[i] < self.list[p]):  
            self.swap(i, p)
            self.min_heapify_up(p)

    def push(self, v): 
        last = self.size
        self.size += 1
        self.list.append(v) 
        self.index[v.name] = last 
        self.min_heapify_up(last)

    def decreaseKey(self, i, new_val):
        self.list[i].key  = new_val 
        self.min_heapify_up(i)

    def get_index(self, v): 
        return self.index.get(v, -1)
    
    def get_element(self, v): 
        i = self.get_index(v)
        return self.list[i] if i >= 0 else None

    def __len__(self):
        return self.size
'''