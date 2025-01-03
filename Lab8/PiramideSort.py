# б ) Реалiзувати алгоритм пiрамiдального сортування та продемонструвати його роботу з
# даними рiзного розмiру.

import time
import matplotlib.pyplot as plt
from copy import deepcopy

from RandomLists import RandomLists


class PiramideSort:
    def __init__(self, array=None):
        if array is None:
            self.array = []
        else:
            self.__dict__ = self.heapify(array).__dict__

    def _swap(self, index_from: int, index_to: int) -> None:
        self.array[index_from], self.array[index_to] = self.array[index_to], self.array[index_from]

    def _sift_up(self, index: int) -> None:
        element = self.array[index]
        parent = (index-1)//2
        element_parent = self.array[parent]
        while element < element_parent and parent != -1:
            self._swap(index, parent)
            index = parent
            element = self.array[index]
            parent = (index-1)//2
            element_parent = self.array[parent]

    def _sift_down(self, index: int) -> None:
        child_left = 2*index + 1
        child_right = 2*index + 2
        length = len(self.array)
        if child_left < length:
            if child_left == length - 1:
                if self.array[index] > self.array[child_left]:
                    self._swap(index, child_left)
                return

            if self.array[child_left] <= self.array[child_right]:
                check_first = child_left
                check_second = child_right
            else:
                check_first = child_right
                check_second = child_left

            if self.array[index] > self.array[check_first]:
                self._swap(index, check_first)
                self._sift_down(check_first)
            elif self.array[index] > self.array[check_second]:
                self._swap(index, check_second)
                self._sift_down(check_second)

    def deepcopy(self):
        return deepcopy(self)

    def insert(self, value: int) -> None:
        length = len(self.array)
        self.array.append(value)
        self._sift_up(length)

    def delete(self):
        last_elem = self.array.pop()
        if self.array:
            elem_to_pop = self.array[0]
            self.array[0] = last_elem
            self._sift_down(0)
            return elem_to_pop
        return last_elem

    @property
    def peek(self):
        return self.array[0]

    def heapify(self, array):  # TODO _sift_down
        ps_new = self.__class__()
        for element in array:
            ps_new.insert(element)
        return ps_new

    def search(self, value: int):
        if value in self.array:
            return self.array.index(value)
        return -1

    def extract_max(self):  # ? TODO _sift_?
        index_last_non_leaf = (len(self.array) - 1) // 2
        leafs = self.array[index_last_non_leaf:]
        index_leaf_max = leafs.index(max(leafs))
        return self.array.pop(index_leaf_max + index_last_non_leaf)

    def extract_min(self):
        return self.delete()

    def update(self, index: int, value: int):
        old_element = self.array[index]
        self.array[index] = value
        if value > old_element:
            self._sift_down(index)
        elif value < old_element:
            self._sift_up(index)

    def sort(self, inline=False, details_need=False):
        start_time = time.time()
        array_sorted = [0] * len(self.array)
        index = 0
        if not inline:
            ps_copy = self.deepcopy()
            while ps_copy:
                array_sorted[index] = ps_copy.delete()
                index += 1
        else:
            while self:
                array_sorted[index] = self.delete()
                index += 1
        ps_sorted = self.heapify(array_sorted)
        if inline:
            self.__dict__ = ps_sorted.__dict__
        if details_need:
            to_return = {"Time": time.time() - start_time, "Name": "PiramideSort"}  #, "Equations": _equations, "Memory": _memory, "Swaps": _swaps}
            return ps_sorted, to_return
        return ps_sorted

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return str(self.array)


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

    print(f'[{bar}] {percentage}% ETA: {etc}', flush=True, end='\r')
    if ready == overal:
        print(f'[{bar}] {percentage}% ETA: FINISHED                                                                                    ', flush=True, end='\r')
        print()


if __name__ == '__main__':
    types = ['sorted', 'random', 'almostsorted', 'reverse', 'somenumbers', 'triangular']
    numbers = [1*10**2, 3*10**2, 5*10**2, 10**3, 3*10**3]  # , 5*10**3, 5*10**2, 10**3, 3*10**3, 5*10**3, 10**4
    numbers = [1*10**2, 3*10**2, 5*10**2, 10**3, 3*10**3, 5*10**3, 5*10**2, 10**3, 3*10**3, 5*10**3, 10**4]  # , 5*10**3, 5*10**2, 10**3, 3*10**3, 5*10**3, 10**4
    numbers = [100, 500, 1000]
    numbers = [100, 500, 1000, 10000, 50000, 100000, 500000]
    tries = 50
    tries = 100

    measurements = ["Time"]

    overal = len(types) * len(numbers) * tries
    ready = 0
    estimated_time = float("inf")

    typs = dict()
    nums = dict()
    trs = dict()

    for typ in types:
        for measurement in measurements:
            nums[measurement] = []
        for number in numbers:
            for measurement in measurements:
                trs[measurement] = []

            for _ in range(tries):
                array = RandomLists(number, typ)
                dct_of_result = PiramideSort(array.list).sort(True, True)[1]
                ready += 1
                progressbar(ready, overal, estimated_time)

                for measurement in measurements:
                    trs[measurement].append(dct_of_result[measurement])
            for measurement in measurements:
                nums[measurement].append(sum(trs[measurement]) / len(trs[measurement]))
            if 'Time' in measurements:
                estimated_time = (overal - ready) * sum(trs['Time']) / len(trs['Time'])

        typs[typ] = nums.copy()

    # print(typs)
    for measurement in measurements:
        for typ, nums in typs.items():
            print(typ, nums)
            plt.plot(numbers, nums[measurement], label=typ)
        plt.legend()
        plt.xlabel("Size")
        plt.ylabel(measurement)

        # plt.show()

        plt.savefig("./Lab8/Results/" + measurement + "_" + str(len(numbers)) + "_" + "numbers" + ".png")
        plt.clf()
