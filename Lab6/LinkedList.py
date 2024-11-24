import sys
from copy import copy as cp, deepcopy as dcp


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def copy(self):
        return cp(self)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data

    def __lt__(self, other):
        if not isinstance(other, Node):
            return False
        # print(self.data, other.data, self.data < other.data)
        return self.data < other.data

    def __gt__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data > other.data

    def __le__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data <= other.data

    def __ne__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data != other.data

    def __ge__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data >= other.data

    def __sizeof__(self):
        # size = sys.getsizeof(self)
        size = sys.getsizeof(self.data)
        # size += sys.getsizeof(self.next)
        return size

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def add(self, data):
        if isinstance(data, Node):
            node = data.copy()
            node.next = None
        else:
            node = Node(data)
        if self.head is None:
            self.head = node
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = node
        self.size += 1

    def remove(self, data):
        node = self.head
        prev = None
        while node:
            if node.data == data:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                self.size -= 1
                return
            prev = node
            node = node.next

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next

    def __setitem__(self, index, data):
        if isinstance(index, int):
            node = self[index]
            if isinstance(data, Node):
                node.data = data.data
            else:
                node.data = data
        elif isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = self.size if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if start < 0 or stop < 0 or step == 0:
                raise IndexError
            if start >= self.size:
                start = self.size
            if stop > self.size:
                stop = self.size
            for i in range(start, stop, step):
                node = self[i]
                if isinstance(data, Node):
                    node.data = data.data
                elif isinstance(data, list):
                    if stop - start != len(data):
                        raise IndexError
                    if isinstance(data[i], Node):
                        node.data = data[i].data
                    else:
                        node.data = data[i]
                elif isinstance(data, LinkedList):
                    node.data = data[i]
                else:
                    node.data = data
    def __getitem__(self, index):
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = self.size if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if start < 0 or stop < 0 or step == 0:
                raise IndexError
            if start >= self.size:
                start = self.size
            if stop > self.size:
                stop = self.size
            result = LinkedList()
            for i in range(start, stop, step):
                result.add(self[i])
            return result

        elif isinstance(index, int):
            if index < 0 or index >= self.size:
                raise IndexError
            node = self.head
            for i in range(index):
                node = node.next
            return node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __sizeof__(self):
        node = self.head
        size = 0
        while node:
            size += sys.getsizeof(node)
            node = node.next
        return size

    def __len__(self):
        return self.size

    def __repr__(self):
        text = ''
        node = self.head
        while node:
            text += str(node) + ' '
            node = node.next
        return f"[{", ".join(text.split())}]"

    # def __str__(self):
    #     text = ''
    #     node = self.head
    #     while node:
    #         text += str(node) + ' '
    #         node = node.next
    #     return text


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)
    print(linked_list[:3])
    print(linked_list[3:])
    node1 = Node(3)
    node2 = Node(4)
    node1.next = node2
    print(node1 < node2)
    linked_list[:2] = LinkedList(node1, 2)
    print(linked_list)
