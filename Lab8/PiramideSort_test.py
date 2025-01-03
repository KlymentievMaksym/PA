import unittest

from PiramideSort import PiramideSort


class PiramideSortTest(unittest.TestCase):

    _ARRAYS = [
        [3, 5, 8, 9, 4, 9, 7, 2, 6],
        [6, 5, 8, 6, 4, 9, 7, 6, 3],
        [3, 3, 3, 4, 3, 3, 3, 3, 3],
        [7, 2, 1, 8, 6, 3, 5, 4],
        [5, 4, 3],
        [9, 5, 1, 0, 6, 3, 1, 1, 1, 4]
    ]

    def test_insert(self):
        ps = PiramideSort()
        ps.insert(100)
        ps.insert(1)
        self.assertEqual(ps.array, [1, 100])

    def test_delete(self):
        ps = PiramideSort([1, 100])
        ps.delete()
        self.assertEqual(ps.array, [100])

    def test_peek(self):
        ps = PiramideSort([1, 100])
        elem = ps.peek
        self.assertEqual(elem, 1)

    def test_heapify(self):
        ps = PiramideSort().heapify([1, 100])
        self.assertEqual(ps.array, [1, 100])

    def test_search(self):
        ps = PiramideSort([1, 100])
        index = ps.search(100)
        self.assertEqual(index, 1)

    def test_search_wrong(self):
        ps = PiramideSort([1, 100])
        index = ps.search(10)
        self.assertEqual(index, -1)

    def test_extract_max(self):
        ps = PiramideSort([1, 100])
        elem = ps.extract_max()
        self.assertEqual((ps.array, elem), ([1], 100))

    def test_extract_min(self):
        ps = PiramideSort([1, 100])
        elem = ps.extract_min()
        self.assertEqual((ps.array, elem), ([100], 1))

    def test_update(self):
        ps = PiramideSort([1, 100])
        ps.update(0, 101)
        self.assertEqual(ps.array, [100, 101])

    def test_sort(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = PiramideSort(array)
                actual.sort(True)
                self.assertEqual(actual.array, expected)


if __name__ == "__main__":
    unittest.main()
