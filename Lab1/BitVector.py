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

    def check_values(self, value: int):
        if not isinstance(value, (int, np.int32)):
            raise TypeError(f"Value {value} is not an integer")
        elif value > self.max_value:
            raise ValueError(f"Value {value} is too big")
        elif value < 0:
            raise ValueError(f"Value {value} is too small")

    def check_sets(self, other: 'BitVectorSet'):
        if not isinstance(other, BitVectorSet):
            raise TypeError("Other is not a BitVectorSet")
        else:
            can_be_compared = 1
            dict_to_check = {
                "Sizes": self.size == other.size,
                "Register values": self.register_value == other.register_value,
            }

            for key, check in dict_to_check.items():
                can_be_compared -= not check
                if not can_be_compared:
                    raise ValueError(f"{key} are not equal")

    def insert(self, value: int):
        self.check_values(value)

        bit_vector_to_place = int(np.floor(value / self.register_value))
        bit_to_place = value % self.register_value

        self.bits[bit_vector_to_place] = self.bits[bit_vector_to_place] | (1 << bit_to_place)

    def delete(self, value: int):
        self.check_values(value)

        bit_vector_to_delete = int(np.floor(value / self.register_value))
        bit_to_delete = value % self.register_value

        self.bits[bit_vector_to_delete] = self.bits[bit_vector_to_delete] & ~(1 << bit_to_delete)

    def search(self, value: int):
        self.check_values(value)

        bit_vector_to_check = int(np.floor(value / self.register_value))
        bit_to_check = value % self.register_value

        return self.bits[bit_vector_to_check] & (1 << bit_to_check)

    def clear(self):
        old_bit_vector_set = self.bits.copy()

        self.bits = [0b0] * self.size

        return old_bit_vector_set

    def union(self, other: 'BitVectorSet'):
        self.check_sets(other)
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] | other.bits[bit_vector_number]

        return old_bit_vector_set

    def intersection(self, other: 'BitVectorSet'):
        self.check_sets(other)
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] & other.bits[bit_vector_number]

        return old_bit_vector_set

    def set_difference(self, other: 'BitVectorSet'):
        self.check_sets(other)
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] & ~other.bits[bit_vector_number]

        return old_bit_vector_set

    def sym_difference(self, other: 'BitVectorSet'):
        self.check_sets(other)
        old_bit_vector_set = self.bits.copy()

        for bit_vector_number in range(self.size):
            self.bits[bit_vector_number] = self.bits[bit_vector_number] ^ other.bits[bit_vector_number]

        return old_bit_vector_set

    def is_subset(self, other: 'BitVectorSet'):
        self.check_sets(other)
        is_subset = 0

        for bit_vector_number in range(self.size):
            result = self.bits[bit_vector_number] | ~other.bits[bit_vector_number]
            is_subset += (bin(result) == '-0b1')

        return int(np.floor(is_subset/self.size))

    def __str__(self):
        str_to_give = "[ "
        for bit in self.bits:
            str_to_give += str(bin(bit)) + " "
        str_to_give += "]"
        return str_to_give


if __name__ == "__main__":
    np.random.seed(0)

    list_of_18_lists = []
    random_numbers = []

    iterations_for_data = 1000
    iterations_for_time = 300

    size_start = 1000
    size_end = 30000
    size_step = 300

    for j in range(size_end//size_step):
        list_of_18_lists.append([np.random.randint(0, 64 * (size_step*j + size_start) - 1, iterations_for_data) for _ in range(iterations_for_data)])
        random_numbers.append(np.random.randint(0, 64 * (size_step*j + size_start) - 1, iterations_for_data))

    import time
    import matplotlib.pyplot as plt

    i_for_search = np.array([])
    time_for_search = np.array([])
    for i in range(size_start, size_end, size_step):
        start = time.time()
        for _ in range(iterations_for_time):
            BitVectorSet(*(list_of_18_lists[0][i//500-1]), size=i).search(random_numbers[0][i//500-1])
        end = time.time()
        i_for_search = np.append(i_for_search, i)
        time_for_search = np.append(time_for_search, ((end - start) / iterations_for_time * 10**3))
    figure, axis = plt.subplots()
    axis.plot(i_for_search, time_for_search)
    axis.set_title("Search time")
    axis.set_xlabel("Розмір множини")
    axis.set_ylabel("Час виконання, мс")
    plt.show()

    i_for_search = np.array([])
    time_for_search = np.array([])
    for i in range(size_start, size_end, size_step):
        index_for_second_bit_vector = int(np.random.randint(0, size_end//size_step, 1)[0])
        start = time.time()
        for _ in range(iterations_for_time):
            BitVectorSet(*(list_of_18_lists[0][i//500-1]), size=i).sym_difference(BitVectorSet(*(list_of_18_lists[0][index_for_second_bit_vector]), size=i))
        end = time.time()
        i_for_search = np.append(i_for_search, i)
        time_for_search = np.append(time_for_search, ((end - start) / iterations_for_time * 10**3))
    figure, axis = plt.subplots()
    axis.plot(i_for_search, time_for_search)
    axis.set_title("SymDifference time")
    axis.set_xlabel("Розмір множини")
    axis.set_ylabel("Час виконання, мс")
    plt.show()
