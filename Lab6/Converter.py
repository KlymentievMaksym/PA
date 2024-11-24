from LinkedList import LinkedList


class Converter:
    def array_to_linked_list(array):
        linked_list = LinkedList()
        for element in array:
            linked_list.add(element)
        return linked_list

    def linked_list_to_array(linked_list):
        array = []
        node = linked_list.head
        while node:
            array.append(node.data)
            node = node.next
        return array


if __name__ == '__main__':
    print(Converter.array_to_linked_list([1, 2, 3, 4, 5]))
    converter = Converter
    print([1, 2, 3, 4, 5])
    linked_list = converter.array_to_linked_list([1, 2, 3, 4, 5])
    print(linked_list, len(linked_list))
    linked_list.remove(3)
    print(linked_list, len(linked_list))
    array = converter.linked_list_to_array(linked_list)
    print(array)