from numpy import random
from RandomLists import RandomLists
import time
import sys


class QuickSort:
    def __init__(self):
        """Словники для вибору опорного елемента та схеми розбиття"""
        self._PIVOT = {'LAST': self._last_pivot, 'RANDOM': self._random_pivot, 'MID': self._mid_pivot, 'MID3': self._mid3_pivot}
        self._SCHEME = {'LOMUTE': self._lomute, 'HOAR': self._hoar}

    def _swap(self, array, i, j):
        """Функцiя перестановки індексів двох елементiв"""
        array[i], array[j] = array[j], array[i]
        return array

    def _last_pivot(self, array):
        """Останній елемент (Невідсортований)"""
        return len(array)-1

    def _random_pivot(self, array):
        """Випадковий елемент (Невідсортований)"""
        return random.randint(0, len(array))

    def _mid_pivot(self, array):
        """Медіана з початку, середини та кінця (Відсортованих?)"""
        mid3 = [array[0], array[len(array)//2], array[-1]]
        mid3_indexes = [0, len(array)//2, -1]
        for i in range(3):
            for j in range(i+1, 3):
                if mid3[i] > mid3[j]:
                    self._swap(mid3, i, j)
                    self._swap(mid3_indexes, i, j)
        return mid3_indexes[1]

    def _mid3_pivot(self, array):
        """Медіана з трьох елементів (Відсортованих?)"""
        array_copy = array.copy()
        mid3 = []
        mid3_indexes = []
        for i in range(3):
            mid3_indexes.append(random.randint(0, len(array)))
            mid3.append(array_copy.pop(mid3_indexes[i]))
        for i in range(3):
            for j in range(i+1, 3):
                if mid3[i] > mid3[j]:
                    self._swap(mid3, i, j)
                    self._swap(mid3_indexes, i, j)
        return mid3_indexes[1]

    def _choose_pivot(self, array, pivot):
        """4 методи вибору опорного елемента"""
        if pivot.upper() in self._PIVOT.keys():
            return self._PIVOT[pivot.upper()](array)
        else:
            raise ValueError("Pivot can be only LAST, RANDOM, MID or MID3")

    def _choose_scheme(self, scheme):
        """2 схеми розбиття"""
        if scheme.upper() in self._SCHEME.keys():
            return self._SCHEME[scheme.upper()]
        else:
            raise ValueError("Scheme can be only LOMUTE or HOAR")

    def _lomute(self, array, pivot_type, _equations, _memory, _swaps):
        """Алгоритм швидкого сортування зi схемою розбиття Ломуто"""
        pivot = self._choose_pivot(array, pivot_type)
        if len(array) <= 1:
            return array, _equations, _memory, _swaps

        i, j = -1, 0
        _memory += sys.getsizeof(i)
        _memory += sys.getsizeof(j)

        _equations += 1
        # print(f"i = {i}, j = {j}, pivot = {pivot}")
        if array[j] <= array[pivot]:
            i += 1
            if i != j:
                _swaps += 1
                self._swap(array, i, j)

        # print("Entering while loop")

        while j < len(array) - 2:
            # print(f"i = {i}, j = {j}, pivot = {pivot}")
            j += 1
            _equations += 1
            if array[j] <= array[pivot]:
                i += 1
                if i != j:
                    _swaps += 1
                    # print(f"i = {i}, SWAP = {array[i]}, j = {j}, SWAP = {array[j]}")
                    self._swap(array, i, j)
        i += 1
        _swaps += 1
        # print(f"i = {i}, SWAP = {array[i]}, pivot = {pivot}, SWAP = {array[pivot]}")
        self._swap(array, i, pivot)

        array[:i], _equations, _memory, _swaps = self._lomute(array[:i], pivot_type, _equations, _memory, _swaps)
        array[i+1:], _equations, _memory, _swaps = self._lomute(array[i+1:], pivot_type, _equations, _memory, _swaps)

        return array, _equations, _memory, _swaps

    def _hoar(self, array, pivot_type, _equations, _memory, _swaps, _depth=0):
        """Алгоритм швидкого сортування зi схемою розбиття Гоара"""
        if len(array) <= 1:
            return array, _equations, _memory, _swaps
        if len(array) == 2:
            if array[0] > array[1]:
                _swaps += 1
                self._swap(array, 0, 1)
            return array, _equations, _memory, _swaps
        pivot = self._choose_pivot(array, pivot_type)
        t, i, j = array[pivot], 0, len(array)-1
        while i < j:
            if i == pivot:
                i += 1
            if j == pivot:
                j -= 1
            while array[i] < t and i < j:
                _equations += 1
                i += 1
            while array[j] > t and i <= j:
                _equations += 1
                j -= 1
            if i < j:
                _swaps += 1
                self._swap(array, i, j)
        array[:j], _equations, _memory, _swaps = self._hoar(array[:j], pivot_type, _equations, _memory, _swaps, _depth + 1)
        array[j+1:], _equations, _memory, _swaps = self._hoar(array[j+1:], pivot_type, _equations, _memory, _swaps, _depth + 1)

        return array, _equations, _memory, _swaps
        # , start=None, end=None
        # if start is None:
        #     start = 0
        # if end is None:
        #     end = len(array) - 1

        # if start >= end:
        #     return array, _equations, _memory, _swaps

        # if end - start == 1:
        #     if array[start] > array[end]:
        #         _swaps += 1
        #         self._swap(array, start, end)
        #     return array, _equations, _memory, _swaps

        # using_area = array[start:end+1]

        # pivot = self._choose_pivot(using_area, pivot_type)
        # print(f"array = {array}, pivot = {pivot}, start = {start}, end = {end}, _depth = {_depth}")

        # r = using_area[pivot]
        # _memory += sys.getsizeof(r)
        # i = start
        # _memory += sys.getsizeof(i)
        # j = end
        # _memory += sys.getsizeof(j)

        # new_pivot = pivot
        # swap_was = False
        # while i < j:
        #     print(f"r = {r}, i = {i}, j = {j}")
        #     while array[i] <= r and i < j:
        #         _equations += 1
        #         i += 1
        #     _equations += 1
        #     while array[j] > r and i < j:
        #         _equations += 1
        #         j -= 1
        #     _equations += 1
        #     if i < j:
        #         _swaps += 1
        #         self._swap(array, i, j)
        #         swap_was = True

        # print(f"i = {i}, j = {j}, r = {r}")

        # # if i > start:
        # #     _equations, _memory, _swaps = self._hoar(array, pivot_type, _equations, _memory, _swaps, start, i - 1, _depth + 1)
        # # if j < end:
        # #     _equations, _memory, _swaps = self._hoar(array, pivot_type, _equations, _memory, _swaps, j + 1, end, _depth + 1)

        # if swap_was:
        #     array, _equations, _memory, _swaps = self._hoar(array, pivot_type, _equations, _memory, _swaps, start, i - 1, _depth + 1)
        #     array, _equations, _memory, _swaps = self._hoar(array, pivot_type, _equations, _memory, _swaps, j + 1, end, _depth + 1)
        #     # _equations, _memory, _swaps = self._hoar(array, pivot_type, _equations, _memory, _swaps, j + 1, end + 1, _depth + 1)

        # return array, _equations, _memory, _swaps

    #     t, i, j = array[pivot], 0, len(array)-1
    #     _memory += sys.getsizeof(i)
    #     _memory += sys.getsizeof(j)

    #     while array[i] < t and i < j:
    #         _equations += 1
    #         i += 1
    #     _equations += 1
    #     while array[j] > t and i < j:
    #         _equations += 1
    #         j -= 1
    #     _equations += 1
    #     if i < j:
    #         _swaps += 1
    #         self._swap(array, i, j)
    #         while i < j:
    #             while array[i] < t and i < j:
    #                 _equations += 1
    #                 i += 1
    #             _equations += 1
    #             while array[j] > t and i < j:
    #                 _equations += 1
    #                 j -= 1
    #             _equations += 1
    #             if i < j:
    #                 _swaps += 1
    #                 self._swap(array, i, j)


    #     new_pivot = j
    #     return array, new_pivot, _equations, _memory, _swaps

    def standard_quicksort(self, array, scheme_type='lomute', pivot_type='last', time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _swaps=0):
        """а) Реалiзувати Алгоритм швидкого сортування (з пiдтримкою обчислення часу виконання, кiлькостi проведених порiвнянь, операцiй переставляння елементiв та використаної пам’ятi)."""
        pivot = self._choose_pivot(array, pivot_type)
        scheme = self._choose_scheme(scheme_type)

        if inplace:
            result = array
        else:
            result = array.copy()
            _memory += sys.getsizeof(result)

        if time_count:
            start = time.time()
            _memory += sys.getsizeof(start)

        # result, _equations, _memory, _swaps = self._recursive(result, scheme, pivot, pivot_type, _equations, _memory, _swaps)
        result, _equations, _memory, _swaps = scheme(result, pivot_type, _equations, _memory, _swaps)

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": scheme_type.capitalize() + pivot_type.capitalize()}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": scheme_type.capitalize() + pivot_type.capitalize()}

        if inplace:
            array[:] = result

        if details_need:
            return result, to_return

        return result
        

if __name__ == "__main__":
    quick_sort = QuickSort()
    # sorted, random, almostsorted, reverse, somenumbers, triangular
    array = RandomLists(10, 'random', disorder_level=0.4, start=0)
    # print(array.list)
    # LAST, RANDOM, MID or MID3 .list
    print(quick_sort.standard_quicksort(array.list, scheme_type='lomute', pivot_type='last', time_count=True, details_need=True))
    # array = [3, 5, 8, 9, 4, 9, 7, 2, 6]
    # array = [3, 3, 3, 4, 3, 3, 3, 3, 3]
    # array = [7, 2, 1, 8, 6, 3, 5, 4]
    # array = [5, 4, 3]
    # print(quick_sort.standard_quicksort(array.list, time_count=True, details_need=True))
    # print(quick_sort.standard_quicksort(array, scheme_type='hoar', pivot_type='last', time_count=True, details_need=True))
