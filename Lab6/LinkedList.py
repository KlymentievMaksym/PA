class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
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

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self.size

    def __str__(self):
        text = ''
        node = self.head
        while node:
            text += str(node) + ' '
            node = node.next
        return text