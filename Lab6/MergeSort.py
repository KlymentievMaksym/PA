# а) Реалiзувати рекурсивний (Top-Down MergeSort) та iтеративний (Bottom-Up MergeSort)
# варiанти алгоритму сортування злиттям (з пiдтримкою обчислення часу виконання,
# кiлькостi проведених порiвнянь, операцiй“копiювань” та використаної пам’ятi)

# в) Реалiзувати додатково третiй варiант алгоритму сортування злиттям, який має бути
# iтеративним з оптимiзацiями cutoff(-to-insertion), stop-if-already-sorted та eliminate-the-
# copy-to-the-auxiliary-array.

# г) Реалiзувати додатково четвертий варiант алгоритму сортування злиттям, який має бути
# iтеративним, але з подiлом на 10 частин, а не 2 частини. Замiсть такого варiанту можна
# реалiзувати алгоритм сортування злиттям для зв’язного списку, а не масиву.

# д) Виконати порiвняльний аналiз (з даними рiзного розмiру) всiх чотирьох варiантiв
# алгоритму сортування злиттям вiдносно часу виконання, кiлькостi проведених
# порiвнянь, операцiй“копiювань” та використаної пам’ятi.

import time
import sys

from RandomLists import RandomLists
from LinkedList import LinkedList
from Converter import Converter


class MergeSort:
    def _merge(self, left, right, _equations, _memory, _copies):
        result = []
        i, j = 0, 0
        size_left, size_right = len(left), len(right)

        _memory += sys.getsizeof(i)
        _memory += sys.getsizeof(j)
        _memory += sys.getsizeof(size_left)
        _memory += sys.getsizeof(size_right)

        while i < size_left and j < size_right:  # min(size_left, size_right)
            _equations += 1
            if left[i] < right[j]:
                result.append(left[i])
                _copies += 1
                i += 1
            else:
                result.append(right[j])
                _copies += 1
                j += 1
        if i < size_left:  # 1
            result.extend(left[i:])
            _copies += len(left[i:])
        elif j < size_right:  # 1
            result.extend(right[j:])
            _copies += len(right[j:])

        # _equations += 3 + min(size_left, size_right)
        # _memory += sys.getsizeof(result)

        return result, _equations, _memory, _copies

    def recursive_merge_sort(self, array, time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _copies=0, _depth=0):
        """а) Реалiзувати рекурсивний (Top-Down MergeSort)"""

        if time_count:
            start = time.time()
            _memory += sys.getsizeof(start)

        if len(array) <= 1 and _depth != 0:
            return array, _equations, _memory, _copies

        mid = len(array) // 2
        _memory += sys.getsizeof(mid)
        left, _equations, _memory, _copies = self.recursive_merge_sort(array[:mid], False, False, False, _equations, _memory, _copies, _depth+1)
        _copies += len(left)
        _memory += sys.getsizeof(left)
        right, _equations, _memory, _copies = self.recursive_merge_sort(array[mid:], False, False, False, _equations, _memory, _copies, _depth+1)
        _copies += len(right)
        _memory += sys.getsizeof(right)
        result, _equations, _memory, _copies = self._merge(left, right, _equations, _memory, _copies)
        _memory += sys.getsizeof(result)

        if _depth != 0:
            return result, _equations, _memory, _copies

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "Recursive"}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "Recursive"}
        _memory += sys.getsizeof(to_return)

        if not details_need:
            return result

        if inplace:
            array[:] = result

        return result, to_return

    def iterative_merge_sort(self, array, time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _copies=0):
        """а) Реалiзувати iтеративний (Bottom-Up MergeSort)"""

        if inplace:
            result = array
        else:
            result = array.copy()
            _copies += len(result)
            _memory += sys.getsizeof(result)

        if time_count:
            start = time.time()

        n = len(array)
        _memory += sys.getsizeof(n)

        length = 1
        _memory += sys.getsizeof(length)
        while length <= n//2:
            for i in range(0, n, length*2):
                j = i + length

                left = result[i:j]
                _copies += len(left)
                _memory += sys.getsizeof(left)
                right = result[j:j+length]
                _copies += len(right)
                _memory += sys.getsizeof(right)

                if left != [] and right != []:
                    result[i:j+length], _equations, _memory, _copies = self._merge(left, right, _equations, _memory, _copies)
            length *= 2

        left = result[:length]
        _copies += 1
        _memory += sys.getsizeof(left)
        right = result[length:]
        _copies += 1
        _memory += sys.getsizeof(right)

        result, _equations, _memory, _copies = self._merge(left, right, _equations, _memory, _copies)
        _memory += sys.getsizeof(result)

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "Iterative"}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "Iterative"}
        _memory += sys.getsizeof(to_return)

        if not details_need:
            return result

        return result, to_return

    def iterative_cutoff_stop_eliminate_merge_sort(self, array, time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _copies=0):
        """в) Реалiзувати додатково третiй варiант алгоритму сортування злиттям, який має бути iтеративним з оптимiзацiями cutoff(-to-insertion), stop-if-already-sorted та eliminate-the-copy-to-the-auxiliary-array"""
        pass
        # if inplace:
        #     result = array
        # else:
        #     result = array.copy()
        #     _copies += len(result)
        #     _memory += sys.getsizeof(result)

        # if time_count:
        #     start = time.time()

        # n = len(array)
        # _memory += sys.getsizeof(n)

        # length = 7
        # _memory += sys.getsizeof(length)
        # while length <= n//2:
        #     for i in range(0, n, length*2):
        #         j = i + length

        #         left = result[i:j]
        #         if i == 0:
        #             left = insertion_sort(left)
        #             _equations += 2
        #             _memory += sys.getsizeof(left)
        #         _copies += len(left)
        #         _memory += sys.getsizeof(left)
        #         right = result[j:j+length]
        #         _copies += len(right)
        #         _memory += sys.getsizeof(right)

        #         if left != [] and right != []:
        #             result[i:j+length], _equations, _memory, _copies = self._merge(left, right, _equations, _memory, _copies)
        #     length *= 2

        left = result[:length]
        _copies += 1
        _memory += sys.getsizeof(left)
        right = result[length:]
        _copies += 1
        _memory += sys.getsizeof(right)

        result, _equations, _memory, _copies = self._merge(left, right, _equations, _memory, _copies)
        _memory += sys.getsizeof(result)

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "Iterative"}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "Iterative"}
        _memory += sys.getsizeof(to_return)

        if not details_need:
            return result

        return result, to_return

    def _linked_merge(self, linked_list_left, linked_list_right, _equations=0, _memory=0, _copies=0):
        i, j = linked_list_left.head, linked_list_right.head
        _memory += sys.getsizeof(i)
        _memory += sys.getsizeof(j)

        result = LinkedList()

        # print(i, j, i < j)

        while i is not None and j is not None:
            _equations += 1
            if i < j:
                result.add(i.data)
                i = i.next
                _copies += 1
            else:
                result.add(j.data)
                j = j.next
                _copies += 1
        while i is not None:
            result.add(i.data)
            i = i.next
            _copies += 1
        while j is not None:
            result.add(j.data)
            j = j.next
            _copies += 1

        _memory += sys.getsizeof(result)

        return result, _equations, _memory, _copies

    def linked_list_merge_sort(self, linked_list, time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _copies=0, _depth=0):
        """г) Реалiзувати додатково четвертий варiант алгоритму сортування злиттям, алгоритм сортування злиттям для зв’язного списку, а не масиву."""
        if time_count:
            start = time.time()
            _memory += sys.getsizeof(start)

        if len(linked_list) <= 1:
            return linked_list, _equations, _memory, _copies

        mid_index = len(linked_list) // 2
        _memory += sys.getsizeof(mid_index)

        linked_list_left, _equations, _memory, _copies = self.linked_list_merge_sort(linked_list[:mid_index], False, False, False, _equations, _memory, _copies, _depth + 1)
        _copies += len(linked_list_left)
        _memory += sys.getsizeof(linked_list_left)
        linked_list_right, _equations, _memory, _copies = self.linked_list_merge_sort(linked_list[mid_index:], False, False, False, _equations, _memory, _copies, _depth + 1) 
        _copies += len(linked_list_right)
        _memory += sys.getsizeof(linked_list_right)
        result, _equations, _memory, _copies = self._linked_merge(linked_list_left, linked_list_right, _equations, _memory, _copies)

        # print(linked_list_left)
        # print(linked_list_right)
        # print(result)

        if _depth != 0:
            return result, _equations, _memory, _copies

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "LinkedList"}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Copies": _copies, "Name": "LinkedList"}
        _memory += sys.getsizeof(to_return)

        if not details_need:
            return result

        if inplace:
            linked_list[:] = result

        return result, to_return
    

if __name__ == '__main__':
    merge_sort = MergeSort()
    sorts = [merge_sort.recursive_merge_sort, merge_sort.iterative_merge_sort, merge_sort.linked_list_merge_sort]
    types = ['sorted', 'random', 'almostsorted', 'reverse', 'somenumbers']
    numbers = [10, 100]  # , 1000, 10000
    lst = RandomLists(10, 'somenumbers').list
    # print(Converter.array_to_linked_list(lst))
    print(merge_sort.recursive_merge_sort(lst, time_count=True, details_need=True))
    print(merge_sort.iterative_merge_sort(lst, time_count=True, details_need=True))
    print(merge_sort.linked_list_merge_sort(Converter.array_to_linked_list(lst), time_count=True, details_need=True))

    # lst = Converter.array_to_linked_list(lst)
    # print(lst)
    # print(merge_sort.linked_list_merge_sort(lst, time_count=True, details_need=True, inplace=False))
    # print(merge_sort.linked_list_merge_sort(lst, time_count=True, details_need=True, inplace=True))
    # print(lst)

    # for sort in sorts:
    #     for typ in types:
    #         for number in numbers:
    #             if sort == merge_sort.linked_list_merge_sort:
    #                 rng = RandomLists(number, typ, linked_list=True)
    #             else:
    #                 rng = RandomLists(number, typ)
    #             print(rng)
    #             print(sort(rng.list))
