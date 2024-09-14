import numpy as np


class BitVectorSet:
    def __init__(self, *start_numbers, size: int = 1000, register_value: int = 64):
        self.size = size
        self.register_value = register_value
        self.bits = [0b0] * size
        self.max_value = register_value * size - 1
        self.univesum = [bin(register_value - 1)] * size
        for value in start_numbers:
            self.insert(value)

    def time_check(self):
        raise NotImplementedError

    def insert(self, value: int):
        bit_vector_to_place = int(np.floor(value / self.register_value))
        bit_to_place = value % self.register_value

        self.bits[bit_vector_to_place] = self.bits[bit_vector_to_place] | (1 << bit_to_place)

    def delete(self, value: int):
        bit_vector_to_delete = int(np.floor(value / self.register_value))
        bit_to_delete = value % self.register_value

        self.bits[bit_vector_to_delete] = self.bits[bit_vector_to_delete] & ~(1 << bit_to_delete)

    def search(self, value: int):
        bit_vector_to_check = int(np.floor(value / self.register_value))
        bit_to_check = value % self.register_value

        return self.bits[bit_vector_to_check] & (1 << bit_to_check)

    def clear(self):
        old_bit_vector_set = self.bits.copy()

        self.bits = [0b0] * self.size

        return old_bit_vector_set

    def union(self, other: 'BitVectorSet'):
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] | other.bits[bit_vector_number]

        return old_bit_vector_set

    def intersection(self, other: 'BitVectorSet'):
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] & other.bits[bit_vector_number]

        return old_bit_vector_set

    def set_difference(self, other: 'BitVectorSet'):
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] & other.bits[bit_vector_number]

        return old_bit_vector_set

    def sym_difference(self, other: 'BitVectorSet'):
        raise NotImplementedError

    def is_subset(self, other: 'BitVectorSet'):
        raise NotImplementedError

    def __str__(self):
        str_to_give = "[ "
        for bit in self.bits:
            str_to_give += str(bin(bit)) + " "
        str_to_give += "]"
        return str_to_give


if __name__ == '__main__':
    bit_vector = BitVectorSet(1, 3, size=2)
    print(bit_vector)
