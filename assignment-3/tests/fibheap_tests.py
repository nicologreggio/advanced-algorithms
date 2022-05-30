import unittest
from fibheap.fibheap import FibHeap
from fibheap.fibheap_item import FibHeapItem


class FibHeapTest(unittest.TestCase):
    def test_insert(self):
        pq = FibHeap()
        elements = [2, 7, 5, 8, 1, 6, 9, -2, 4]

        for el in elements:
            pq.insert(FibHeapItem(el, el))

        current_size = len(pq)
        expected_size = len(elements)

        self.assertEqual(expected_size, current_size)

    def test_maximum_from_empty(self):
        pq = FibHeap()

        current = pq.maximum()
        expected = None

        self.assertEqual(expected, current)

    def test_existing_maximum(self):
        pq = FibHeap()
        elements = [2, 7, 5, 8, 1, 6, 9, -2, 4]

        for el in elements:
            pq.insert(FibHeapItem(el, el))

        current = pq.maximum()
        expected = FibHeapItem(9, 9)

        self.assertEqual(expected, current)

    def test_extract_maximum_from_empty(self):
        pq = FibHeap()

        current = pq.extract_maximum()
        expected = None
        current_size = len(pq)
        expected_size = 0

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_extract_maximum_all_elements_plus_one_more(self):
        pq = FibHeap()
        elements = [2, 7, 5, 8, 1, 6, 9, -2, 4]

        for el in elements:
            pq.insert(FibHeapItem(el, el))

        current = []
        while len(pq):
            m = pq.extract_maximum()
            current.append(m)

        current.append(pq.extract_maximum())

        expected = [FibHeapItem(el, el) for el in sorted(elements, reverse=True)] + [
            None
        ]

        current_size = len(pq)
        expected_size = 0

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_extract_maximum_one_element(self):
        pq = FibHeap()
        elements = [2, 7, 5, 8, 1, 6, 9, -2, 4]

        for el in elements:
            pq.insert(FibHeapItem(el, el))

        current = pq.extract_maximum()
        expected = FibHeapItem(9, 9)

        current_size = len(pq)
        expected_size = len(elements) - 1

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_extract_maximum_all_elements(self):
        pq = FibHeap()
        elements = [2, 7, 5, 8, 1, 6, 9, -2, 4]

        for el in elements:
            pq.insert(FibHeapItem(el, el))

        current = []
        while len(pq):
            current.append(pq.extract_maximum())

        expected = [FibHeapItem(el, el) for el in sorted(elements, reverse=True)]

        current_size = len(pq)
        expected_size = 0

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_increase_key_one_element(self):
        pq = FibHeap()
        elements = [2, 7, 5, 8, 1, 6, 9, -2, 4]
        items = []

        for el in elements:
            item = FibHeapItem(el, el)
            pq.insert(item)
            items.append(item)

        pq.increase_key(items[0], 10)

        current = pq.extract_maximum()
        expected = FibHeapItem(2, 10)

        self.assertEqual(expected, current)

    def test_increase_key_all_elements(self):
        pq = FibHeap()
        elements = {2: 2, 7: 7, 5: 5, 8: 8, 1: 1, 6: 6, 9: 9, 3: 3, 4: 4}
        items = {}

        for name, key in elements.items():
            item = FibHeapItem(name, key)
            pq.insert(item)
            items[name] = item

        new_elements = {2: 10, 7: 7, 5: 5, 8: 8, 1: 20, 6: 9, 9: 11, 3: 3, 4: 10}

        for name, key in new_elements.items():
            if key != elements[name]:
                pq.increase_key(items[name], key)

        current = []
        while len(pq):
            m = pq.extract_maximum()
            current.append(m)

        expected = [
            FibHeapItem(name, key)
            for name, key in sorted(
                new_elements.items(), key=lambda el: el[1], reverse=True
            )
        ]

        self.assertEqual(expected, current)

    def test_all_operations_many_times(self):
        pq = FibHeap()
        elements = {2: 2, 7: 7, 5: 5, 8: 8, 1: 1, 6: 6, 9: 9, 3: 3, 4: 4}
        increased_elements = {2: 10, 1: 20, 6: 9, 9: 11, 4: 12, 7: 9}
        new_elements = {11: 1, 12: 50, 15: 7}
        increased_new_elements = {11: 80, 15: 51, 3: 81}
        items = {}

        def add(key, value):
            item = FibHeapItem(key, value)
            items[key] = item
            pq.insert(item)

        def increase(key, value):
            item = items[key]
            if value != None:
                pq.increase_key(item, value)

        current = []
        for _ in range(2):
            for key, value in elements.items():
                add(key, elements[key])

            while len(pq) == len(elements) // 2:
                current.append(pq.extract_maximum())

            for key, value in increased_elements.items():
                increase(key, value)

            current.append(pq.extract_maximum())

            for key, value in new_elements.items():
                add(key, value)

            current.append(pq.extract_maximum())

            for key, value in increased_new_elements.items():
                increase(key, value)

            while len(pq):
                current.append(pq.extract_maximum())

            current.append(pq.extract_maximum())

        expected = [
            FibHeapItem(1, 20),
            FibHeapItem(12, 50),
            FibHeapItem(3, 81),
            FibHeapItem(11, 80),
            FibHeapItem(15, 51),
            FibHeapItem(4, 12),
            FibHeapItem(9, 11),
            FibHeapItem(2, 10),
            FibHeapItem(7, 9),
            FibHeapItem(6, 9),
            FibHeapItem(8, 8),
            FibHeapItem(5, 5),
            None,
            FibHeapItem(1, 20),
            FibHeapItem(12, 50),
            FibHeapItem(3, 81),
            FibHeapItem(11, 80),
            FibHeapItem(15, 51),
            FibHeapItem(4, 12),
            FibHeapItem(9, 11),
            FibHeapItem(2, 10),
            FibHeapItem(7, 9),
            FibHeapItem(6, 9),
            FibHeapItem(8, 8),
            FibHeapItem(5, 5),
            None,
        ]

        self.assertEqual(expected, current)


if __name__ == "__main__":
    unittest.main()
