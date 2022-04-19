class PriorityQueueVertex: 
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
            #self.list[i], self.list[min] = self.list[min], self.list[i]
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
        self.index[v.name] = 0
        self.list.pop()
        self.size -= 1
        self.min_heapify(0)
        return min

    def min_heapify_up(self, i): 
        p = self.parent(i)
        if (i > 0 and self.list[i] < self.list[p]):  
            self.swap(i, p)
            #self.list[i], self.list[self.parent(i)] = self.list[self.parent(i)], self.list[i]
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

'''
class MyHeap: 
    def __init__(self, list): 
        self.list = list 
        self.size = len(self.list) - 1 

    def __repr__(self): 
        return "{0}".format(self.list)
        
    def parent(self, i): 
        return (i - 1)// 2 
    
    def left(self, i): 
        return 2*i +1

    def right(self, i): 
        return (2*i) +2

    def min_heapify(self, i): 
        l = self.left(i)
        r = self.right(i)
        if (l <= self.size) and (self.list[l] < self.list[i]): 
            min = l 
        else: 
            min = i 
        if (r <= self.size) and (self.list[r] < self.list[min]): 
            min = r 
        if min != i: 
            #maybe problem here!
            self.list[i], self.list[min] =   self.list[min], self.list[i]
            self.min_heapify(min)

    def build_min_heap(self): 
        for i in reversed(range((self.size//2)+1)): 
            self.min_heapify(i)

    # problem here in the size!
    def extract_min(self): 
        min = self.list[0]
        self.list[0] = self.list[self.size]
        self.list.pop()
        self.size -= 1
        self.min_heapify(0)
        return min

    def min_heapify_up(self, i): 
        if (i > 0 and self.list[i] < self.list[self.parent(i)]):  
            self.list[i], self.list[self.parent(i)] = self.list[self.parent(i)], self.list[i]
            self.min_heapify_up(self.parent(i))
            #self.min_heapify_up(i)

    def push(self, v): 
        self.size += 1
        self.list.append(v) 
        self.min_heapify_up(self.size)

    def decreaseKey(self, i, new_val):
        self.list[i].key  = new_val 
        self.min_heapify_up(i)

'''      