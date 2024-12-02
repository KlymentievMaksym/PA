from numpy import random
import matplotlib.pyplot as plt

from RandomLists import RandomLists
import time
import sys
import os

sys.setrecursionlimit(1500)

if not os.path.exists('./lab7/Results'):
    os.mkdir('./lab7/Results')


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
            mid3_indexes.append(random.randint(0, len(array_copy)))
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
        
        if len(array) == 2:
            if array[0] > array[1]:
                _swaps += 1
                self._swap(array, 0, 1)
            return array, _equations, _memory, _swaps

        if len(array) <= 1:
            return array, _equations, _memory, _swaps

        pivot = self._choose_pivot(array, pivot_type)

        array_pivot = array.pop(pivot)
        i, j = -1, 0
        _memory += sys.getsizeof(array_pivot)
        _memory += sys.getsizeof(i)
        _memory += sys.getsizeof(j)

        _equations += 1
        if array[j] <= array_pivot:
            i += 1
            if i != j:
                _swaps += 1
                self._swap(array, i, j)


        while j < len(array) - 1:
            j += 1
            _equations += 1
            if array[j] <= array_pivot:
                i += 1
                if i != j:
                    _swaps += 1
                    self._swap(array, i, j)
        array.append(array_pivot)
        i += 1
        _swaps += 1
        self._swap(array, i, -1)

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

        t = array.pop(pivot)
        i, j = 0, len(array)-1

        _memory += sys.getsizeof(t)
        _memory += sys.getsizeof(i)
        _memory += sys.getsizeof(j)

        while i < j:
            while array[i] <= t and i < j:
                _equations += 1
                i += 1
            _equations += 1
            while array[j] > t and i < j:
                _equations += 1
                j -= 1
            _equations += 1
            if i < j:
                _swaps += 1
                self._swap(array, i, j)
        _equations += 1
        if j == len(array) - 1 and array[j] <= t:
            array.append(t)
            j += 1
        else:
            array.insert(j, t)

        array[:j], _equations, _memory, _swaps = self._hoar(array[:j], pivot_type, _equations, _memory, _swaps, _depth + 1)
        array[j+1:], _equations, _memory, _swaps = self._hoar(array[j+1:], pivot_type, _equations, _memory, _swaps, _depth + 1)

        return array, _equations, _memory, _swaps

    def standard_quicksort(self, array, scheme_type='lomute', pivot_type='last', time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _swaps=0):
        """а) Реалiзувати Алгоритм швидкого сортування (з пiдтримкою обчислення часу виконання, кiлькостi проведених порiвнянь, операцiй переставляння елементiв та використаної пам’ятi)."""
        pivot = self._choose_pivot(array, pivot_type)
        scheme = self._choose_scheme(scheme_type)

        _memory += sys.getsizeof(pivot)
        _memory += sys.getsizeof(scheme)

        if inplace:
            result = array
        else:
            result = array.copy()
            _memory += sys.getsizeof(result)

        if time_count:
            start = time.time()
            _memory += sys.getsizeof(start)

        result, _equations, _memory, _swaps = scheme(result, pivot_type, _equations, _memory, _swaps)

        if time_count:
            time_result = time.time() - start
            _memory += sys.getsizeof(time_result)
            to_return = {"Time": time_result, "Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": scheme_type.capitalize() + pivot_type.capitalize()}
        else:
            to_return = {"Equations": _equations, "Memory": _memory, "Swaps": _swaps, "Name": scheme_type.capitalize() + pivot_type.capitalize()}

        if details_need:
            return result, to_return

        return result
ф

def progressbar(ready, overal, estimated_time):
    fullness = ready / overal
    txt_to_add = "                              "

    filled_up_Length = round(100 * fullness)
    percentage = round(100 * fullness, 1)

    bar = '=' * filled_up_Length + '-' * (100 - filled_up_Length)

    if estimated_time == float("inf"):
        etc = "N/A"
    if estimated_time // 60 < 1:
        etc = f"{estimated_time:.2f} sec"
    if estimated_time // 60 >= 1:
        etc = f"{int(estimated_time // 60)} min, {estimated_time % 60:.0f} sec"
    if estimated_time // 3600 >= 1:
        etc = f"{int(estimated_time // 3600)} hours, {estimated_time % 3600 // 60:.0f} min"

    etc += txt_to_add

    print(f'[{bar}] {percentage}% ETC: {etc}', flush=True, end='\r')
    if ready == overal:
        print(f'[{bar}] {percentage}% ETC: FINISHED                                                                                    ', flush=True, end='\r')
        print()


if __name__ == "__main__":
    quick_sort = QuickSort()

    types = ['sorted', 'random', 'almostsorted', 'reverse', 'somenumbers', 'triangular']
    pivots = ['last', 'random', 'mid', 'mid3']
    sorts = ['lomute', 'hoar']
    numbers = [100, 300, 500, 1000]
    tries = 50

    overal = len(types) * len(pivots) * len(sorts) * len(numbers) * tries
    ready = 0
    estimated_time = float("inf")

    measurements = ["Time", "Equations", "Memory", "Swaps"]

    srts = dict()
    pvts = dict()
    typs = dict()
    nums = dict()
    trs = dict()

    for sort in sorts:
        for pivot in pivots:
            for typ in types:
                for measurement in measurements:
                    nums[measurement] = []

                for number in numbers:

                    for measurement in measurements:
                        trs[measurement] = []

                    for _ in range(tries):
                        array = RandomLists(number, typ)
                        dct_of_result = quick_sort.standard_quicksort(array.list, scheme_type=sort, pivot_type=pivot, time_count=True, details_need=True)[1]
                        ready += 1
                        progressbar(ready, overal, estimated_time)

                        for measurement in measurements:
                            trs[measurement].append(dct_of_result[measurement])
                    for measurement in measurements:
                        nums[measurement].append(sum(trs[measurement]) / len(trs[measurement]))
                    estimated_time = (overal - ready) * sum(trs['Time']) / len(trs['Time'])

                typs[typ] = nums.copy()
            pvts[pivot] = typs.copy()
        srts[sort] = pvts.copy()

    for measurement in measurements:
        for pivot in pivots:
            for typ in types:
                for sort in sorts:
                    plt.plot(numbers, srts[sort][pivot][typ][measurement], label=f"{sort}")
                plt.xlabel("Size")
                plt.ylabel(measurement)
                plt.legend()
                plt.title(f"Type: {typ}, Pivot: {pivot}")
                # plt.show()
                plt.savefig("./Lab7/Results/" + typ + "_" + measurement + "_" + str(len(sorts)) + "_" + "sorts" + "_" + str(len(numbers)) + "_" + "numbers" + "_" + str(tries) + "_" + str(min(numbers)) + "to" + str(max(numbers)) + ".png")
                plt.clf()

                    # print(f"Type: {typ}, Pivot: {pivot}, Sort: {sort}, Measurement: {measurement}")
                    # print(srts[sort][pivot][typ][measurement])
                    # print()


                    # array = RandomLists(number, typ, disorder_level=0.4, start=1)
                    # print(quick_sort.standard_quicksort(array.list, scheme_type=sort, pivot_type=pivot, time_count=True, details_need=True))

    # sorted, random, almostsorted, reverse, somenumbers, triangular
    # LAST, RANDOM, MID or MID3 .list

    # array = RandomLists(10, 'triangular', disorder_level=0.4, start=1)
    # print(array.list
    # print(quick_sort.standard_quicksort(array.list, scheme_type='lomute', pivot_type='mid', time_count=True, details_need=True))

    # array = [3, 5, 8, 9, 4, 9, 7, 2, 6]
    # array = [3, 3, 3, 4, 3, 3, 3, 3, 3]
    # array = [7, 2, 1, 8, 6, 3, 5, 4]
    # array = [5, 4, 3]
    # array = [9, 5, 1, 0, 6, 3, 1, 1, 1, 4]
    # print(quick_sort.standard_quicksort(array, scheme_type='hoar', pivot_type='last', time_count=True, details_need=True))
