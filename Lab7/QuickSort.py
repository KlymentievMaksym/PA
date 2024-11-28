from numpy import random
import time
import sys


class QuickSort:
    def __init__(self):
        self._PIVOT = {'LAST': self._last_pivot, 'RANDOM': self._random_pivot, 'FIRST': self._first_pivot, 'MID': self._mid_pivot, 'MID3': self._mid3_pivot}
        self._SCHEME = {'LOMUTE': self._lomute, 'HOAR': self._hoar}

    def _swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]
        return array

    def _last_pivot(self, array):
        return array[-1]

    def _first_pivot(self, array):
        return array[0]

    def _mid_pivot(self, array):
        return array[len(array) // 2]

    def _mid3_pivot(self, array):
        array_copy = array.copy()
        mid3 = []
        for i in range(3):
            mid3.append(array_copy.pop(random.randint(0, len(array))))
        for i in range(3):
            for j in range(i+1, 3):
                if mid3[i] > mid3[j]:
                    mid3[i], mid3[j] = mid3[j], mid3[i]
        return mid3[1]

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

    def _lomute(self, array, pivot):
        """Алгоритм швидкого сортування зi схемою розбиття Ломуто"""
        pass

    def _hoar(self, array, pivot):
        """Алгоритм швидкого сортування зi схемою розбиття Гоара"""
        pass

    def standard_quicksort(self, array, scheme='lomute', pivot='last', time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _swaps=0):
        """а) Реалiзувати Алгоритм швидкого сортування (з пiдтримкою обчислення часу виконання, кiлькостi проведених порiвнянь, операцiй переставляння елементiв та використаної пам’ятi)."""
        pivot = self._choose_pivot(array, pivot)
        scheme = self._choose_scheme(scheme)
        if time_count:
            start = time.time()
            _memory += sys.getsizeof(start)
        ### MAIN PART ###
        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": "StandardQuicksort"}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": "StandardQuicksort"}
        return to_return
        

if __name__ == "__main__":
    print("Hello")
