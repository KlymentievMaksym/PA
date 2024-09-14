import unittest
from BitVector import BitVectorSet


class TestBitVectorSet(unittest.TestCase):
    def test_create(self):
        test_bit_vector = BitVectorSet(1, 3)

        self.assertEqual(test_bit_vector.bits, [10] + [0] * 999)

    def test_insert(self):
        test_bit_vector = BitVectorSet(1, 3)

        test_bit_vector.insert(5)

        self.assertEqual(test_bit_vector.bits, [42] + [0] * 999)

    def test_delete(self):
        test_bit_vector = BitVectorSet(1, 3)

        test_bit_vector.delete(3)

        self.assertEqual(test_bit_vector.bits, [2] + [0] * 999)

    def test_search_already_created_numbers(self):
        test_bit_vector = BitVectorSet(1, 3)

        self.assertEqual(test_bit_vector.search(3), 8)

    def test_search_not_created_numbers(self):
        test_bit_vector = BitVectorSet(1, 3)

        test_bit_vector.insert(5)

        self.assertEqual(test_bit_vector.search(5), 32)

    def test_clear_already_created_numbers(self):
        test_bit_vector = BitVectorSet(1, 3)

        test_bit_vector.clear()

        self.assertEqual(test_bit_vector.bits, [0] * 1000)

    def test_clear_not_created_numbers(self):
        test_bit_vector = BitVectorSet(1, 3)

        test_bit_vector.insert(5)
        test_bit_vector.clear()

        self.assertEqual(test_bit_vector.bits, [0] * 1000)

    def test_union(self):
        test_bit_vector1 = BitVectorSet(1, 3)
        test_bit_vector2 = BitVectorSet(2, 4)

        test_bit_vector1.union(test_bit_vector2)

        self.assertEqual(test_bit_vector1.bits, [30] + [0] * 999)

    def test_intersection(self):
        test_bit_vector1 = BitVectorSet(1, 3)
        test_bit_vector2 = BitVectorSet(1, 4)

        test_bit_vector1.intersection(test_bit_vector2)

        self.assertEqual(test_bit_vector1.bits, [2] + [0] * 999)

    def test_set_difference(self):
        test_bit_vector1 = BitVectorSet(1, 3)
        test_bit_vector2 = BitVectorSet(1, 4)

        test_bit_vector1.set_difference(test_bit_vector2)

        self.assertEqual(test_bit_vector1.bits, [8] + [0] * 999)

    def test_sym_difference(self):
        test_bit_vector1 = BitVectorSet(1, 3)
        test_bit_vector2 = BitVectorSet(1, 4)

        test_bit_vector1.sym_difference(test_bit_vector2)

        self.assertEqual(test_bit_vector1.bits, [24] + [0] * 999)

    def test_is_subset(self):
        test_bit_vector1 = BitVectorSet(1, 2, 3)
        test_bit_vector2 = BitVectorSet(1, 3)

        self.assertEqual(test_bit_vector2.is_subset(test_bit_vector1), 1)

    def test_time_check(self):
        pass


if __name__ == '__main__':
    unittest.main()
