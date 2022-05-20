from doubly_linked_list.doubly_linked_list_item import DoublyLinkedListItem


class DoublyLinkedListIterator:
    def __init__(self, item: DoublyLinkedListItem):
        self.item = item

    def __iter__(self):
        return self

    def __next__(self):
        if not self.item:
            raise StopIteration()

        tmp = self.item

        self.item = self.item.right

        return tmp
