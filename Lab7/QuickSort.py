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
        return -1

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
            raise ValueError("Pivot can be only LAST, RANDOM, FIRST, MID or MID3")

    def _choose_scheme(self, scheme):
        """2 схеми розбиття"""
        if scheme.upper() in self._SCHEME.keys():
            return self._SCHEME[scheme.upper()]
        else:
            raise ValueError("Scheme can be only LOMUTE or HOAR")

    def _lomute(self, array, pivot, _equations, _memory, _swaps):
        """Алгоритм швидкого сортування зi схемою розбиття Ломуто"""
        if len(array) == 1:
            return array, _equations, _memory, _swaps

        i, j = -1, 0
        _memory += sys.getsizeof(i)
        _memory += sys.getsizeof(j)

        _equations += 1
        if array[j] <= array[pivot]:
            i += 1
            if i != j:
                _swaps += 1
                self._swap(array, i, j)

        while j < len(array) - 1:
            j += 1
            _equations += 1
            if array[j] <= array[pivot]:
                i += 1
                if i != j:
                    _swaps += 1
                    self._swap(array, i, j)
        i += 1
        _swaps += 1
        self._swap(array, i, pivot)
        return array, _equations, _memory, _swaps

    def _hoar(self, array, pivot, _equations, _memory, _swaps):
        """Алгоритм швидкого сортування зi схемою розбиття Гоара"""
        return array, _equations, _memory, _swaps


    def standard_quicksort(self, array, scheme='lomute', pivot='last', time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _swaps=0):
        """а) Реалiзувати Алгоритм швидкого сортування (з пiдтримкою обчислення часу виконання, кiлькостi проведених порiвнянь, операцiй переставляння елементiв та використаної пам’ятi)."""
        pivot = self._choose_pivot(array, pivot)
        scheme = self._choose_scheme(scheme)

        if inplace:
            result = array
        else:
            result = array.copy()
            _memory += sys.getsizeof(result)

        if time_count:
            start = time.time()
            _memory += sys.getsizeof(start)

        result, _equations, _memory, _swaps = scheme(result, pivot, _equations, _memory, _swaps)

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": "StandardQuicksort"}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": "StandardQuicksort"}
        
        if details_need:
            return result, to_return

        return result
        

if __name__ == "__main__":
    quick_sort = QuickSort()
    array = RandomLists(10, 'triangular', start=1)
    array = [3, 5, 8, 9, 4, 9, 7, 2, 6]
    # print(array.list)
    # print(quick_sort.standard_quicksort(array.list, time_count=True, details_need=True))
    print(quick_sort.standard_quicksort(array, time_count=True, details_need=True))
