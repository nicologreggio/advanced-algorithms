import unittest

from doubly_linked_list.circular_doubly_linked_list import (
    CircularDoublyLinkedList,
    DoublyLinkedListItem,
)


class Item(DoublyLinkedListItem):
    def __init__(self, el):
        super().__init__()
        self.el = el

    def __str__(self):
        return f"{self.el}"

    def __repr__(self) -> str:
        return self.__str__()


class CircularDoublyLinkedListTest(unittest.TestCase):
    def test_init_emptylist(self):
        l = CircularDoublyLinkedList()

        current = len(l)
        expected = 0

        self.assertEqual(expected, current)

    def test_to_list(self):
        l = CircularDoublyLinkedList()
        el1 = Item(5)
        el2 = Item(6)
        l.append(el1)
        l.append(el2)
        self.assertEqual('5', str(el1))
        self.assertEqual('5', repr(el1))
        tt=next(iter(iter(l)))
        self.assertEqual('5', str(tt))
        self.assertEqual('6', repr(l[1]))
        self.assertRaises(IndexError, l.__getitem__, 3)

        current = l.to_list()
        expected = [el1, el2]

        self.assertEqual(expected, current)

    def test_remove_all_elements(self):
        l = CircularDoublyLinkedList()

        elements = [Item(i) for i in range(10)]

        for el in elements:
            l.append(el)

        for el in elements:
            l.remove(el)

        current = l.to_list()
        expected = []
        current_size = len(l)
        expected_size = 0

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_remove_2_elements(self):
        l = CircularDoublyLinkedList()

        elements = [Item(i) for i in range(10)]
        elements_to_remove = [elements[0], elements[4], elements[9]]

        for el in elements:
            l.append(el)

        for el in elements_to_remove:
            l.remove(el)

        current = l.to_list()
        expected = [
            elements[1],
            elements[2],
            elements[3],
            elements[5],
            elements[6],
            elements[7],
            elements[8],
        ]
        current_size = len(l)
        expected_size = 7

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_add_remove_many_elements(self):
        l = CircularDoublyLinkedList()
        elements = [Item(i) for i in range(10)]

        for el in elements:
            l.append(el)

        el1 = Item(5)
        el2 = Item(4)

        l.remove(elements[2])
        l.remove(elements[3])
        l.append(el1)
        l.remove(elements[8])
        l.remove(elements[0])
        l.append(el2)
        l.remove(elements[9])

        current = l.to_list()
        expected = [
            elements[1],
            elements[4],
            elements[5],
            elements[6],
            elements[7],
            el1,
            el2,
        ]
        current_size = len(l)
        expected_size = 7

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)

    def test_clean(self):
        l = CircularDoublyLinkedList()

        elements = [Item(i) for i in range(10)]

        for el in elements:
            l.append(el)

        l.clean()

        current = l.to_list()
        expected = []
        current_size = len(l)
        expected_size = 0

        self.assertEqual(expected, current)
        self.assertEqual(expected_size, current_size)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
