import unittest
from QuickSort import QuickSort

class QuickSort_test(unittest.TestCase):

    _ARRAYS = [
        [3, 5, 8, 9, 4, 9, 7, 2, 6],
        [6, 5, 8, 6, 4, 9, 7, 6, 3],
        [3, 3, 3, 4, 3, 3, 3, 3, 3],
        [7, 2, 1, 8, 6, 3, 5, 4],
        [5, 4, 3],
        [9, 5, 1, 0, 6, 3, 1, 1, 1, 4]
    ]

    def test_quicksort_lomute_last(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='lomute', pivot_type='last')
                self.assertEqual(expected, actual)

    def test_quicksort_lomute_random(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='lomute', pivot_type='random')
                self.assertEqual(expected, actual)

    def test_quicksort_lomute_mid(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='lomute', pivot_type='mid')
                self.assertEqual(expected, actual)

    def test_quicksort_lomute_mid3(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='lomute', pivot_type='mid3')
                self.assertEqual(expected, actual)

    def test_quicksort_hoar_last(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='hoar', pivot_type='last')
                self.assertEqual(expected, actual)

    def test_quicksort_hoar_random(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='hoar', pivot_type='random')
                self.assertEqual(expected, actual)

    def test_quicksort_hoar_mid(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='hoar', pivot_type='mid')
                self.assertEqual(expected, actual)

    def test_quicksort_hoar_mid3(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='hoar', pivot_type='mid3')
                self.assertEqual(expected, actual)

    def test_quicksort_dijkstra_last(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dijkstra', pivot_type='last')
                self.assertEqual(expected, actual)

    def test_quicksort_dijkstra_random(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dijkstra', pivot_type='random')
                self.assertEqual(expected, actual)

    def test_quicksort_dijkstra_mid(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dijkstra', pivot_type='mid')
                self.assertEqual(expected, actual)

    def test_quicksort_dijkstra_mid3(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dijkstra', pivot_type='mid3')
                self.assertEqual(expected, actual)


    def test_quicksort_dual_last(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dual', pivot_type='last')
                self.assertEqual(expected, actual)

    def test_quicksort_dual_random(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dual', pivot_type='random')
                self.assertEqual(expected, actual)

    def test_quicksort_dual_mid(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dual', pivot_type='mid')
                self.assertEqual(expected, actual)

    def test_quicksort_dual_mid3(self):
        for array in self._ARRAYS:
            with self.subTest(msg=f'array={array}'):
                expected = sorted(array)
                actual = QuickSort().standard_quicksort(array, scheme_type='dual', pivot_type='mid3')
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
