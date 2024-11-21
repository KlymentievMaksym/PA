# а) Реалiзувати рекурсивний (Top-Down MergeSort) та iтеративний (Bottom-Up MergeSort)
# варiанти алгоритму сортування злиттям (з пiдтримкою обчислення часу виконання,
# кiлькостi проведених порiвнянь, операцiй“копiювань” та використаної пам’ятi)
import time
import sys



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
            _copies += 1

        return result, to_return

    def iterative_merge_sort(self, array, time_count=False, details_need=False, inplace=False, _equations=0, _memory=0, _copies=0):
        if inplace:
            result = array
        else:
            result = array.copy()
            _copies += 1
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
    

if __name__ == '__main__':
    merge_sort = MergeSort()
    # lst_to_test2 = [1, 2, 3, 4, 5, 6, 7, 8]
    lst_to_test2 = [1, 5, 3, 7, 2, 6, 4, 8]
    # lst_to_test2 = [1]
    # lst_to_test2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # lst_to_test2 = [21, 17, 40, 4, 8, 51, 15]
    list_of_times_iterative = []
    list_of_times_recursive = []

    print(merge_sort.recursive_merge_sort(lst_to_test2, True, True, False))
    print(merge_sort.recursive_merge_sort(lst_to_test2, False, False, False))
    print(lst_to_test2)
    print()
    print(merge_sort.iterative_merge_sort(lst_to_test2, True, True, False))
    print(lst_to_test2)

    # for i in range(100):
    #     with Timer() as t:
    #         (merge_sort.iterative_merge_sort(lst_to_test2.copy()))
    #     list_of_times_iterative.append(t.time_used)
    #     with Timer() as t:
    #         (merge_sort.recursive_merge_sort(lst_to_test2.copy()))
    #     list_of_times_recursive.append(t.time_used)

    # result_for_iterative = sum(list_of_times_iterative)/len(list_of_times_iterative)
    # result_for_recursive = sum(list_of_times_recursive)/len(list_of_times_recursive)
    # # difference = abs(result_for_iterative - result_for_recursive)
    # print(f"Average time for iterative merge sort: {result_for_iterative}")
    # print(f"Average time for recursive merge sort: {result_for_recursive}")
    # print(f"Difference between times: {difference}")
