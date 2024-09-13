class BitVectorSet:
    def __init__(self, size=1000, register_value=64):
        self.size = size
        self.register_value = register_value
        self.bits = [[0]*register_value] * size

    def time_check(self):
        raise NotImplementedError

    def insert(self, value):
        raise NotImplementedError

    def delete(self, value):
        raise NotImplementedError

    def search(self, value):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def union(self, other: 'BitVectorSet'):
        raise NotImplementedError

    def intersection(self, other: 'BitVectorSet'):
        raise NotImplementedError

    def set_difference(self, other: 'BitVectorSet'):
        raise NotImplementedError

    def sym_difference(self, other: 'BitVectorSet'):
        raise NotImplementedError

    def is_subset(self, other: 'BitVectorSet'):
        raise NotImplementedError
