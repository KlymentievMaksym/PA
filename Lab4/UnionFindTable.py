class UnionFindTable:
    def __init__(self, sets=[]):
        len_of_sets = len(sets)
        size_of_sets = 0
        for set in sets:
            size_of_sets += len(set)
        self.r = [0] * size_of_sets
        self.list = [0] * len_of_sets
        self.next = [0] * size_of_sets
        self.size = [0] * len_of_sets
        self.internal_names = {internal_name+1: len_of_sets-1-internal_name for internal_name in range(len_of_sets)}
        self.external_names = {external_name: len_of_sets-1-external_name for external_name in range(len_of_sets-1, -1, -1)}
        self.sets = sets
        for set in sets:
            self.make_set(set)

    def make_set(self, x):
        if isinstance(x, int):
            pass
        else:
            index = self.internal_names[self.sets.index(x)+1]
            for item in x:
                self.r[item-1] = index
                next_item = x.index(item)+1
                if next_item < len(x):
                    self.next[item-1] = x[next_item]
                self.size[index] = len(x)
            self.list[index] = x[0]

    def find(self, x):
        return self.external_names[self.r[x-1]]

    def union(self, x, y):
        A = self.internal_names[x]
        B = self.internal_names[y]
        if self.size[A] > self.size[B]:
            A, B = B, A
        z = self.list[A]
        for _ in range(self.size[A]):
            self.r[z-1] = B
            last = z
            z = self.next[z-1]
        self.next[last-1] = self.list[B]
        self.list[B] = self.list[A]
        self.size[B] += self.size[A]
        self.internal_names[x] = B
        self.external_names[B] = x

        return self

    def print(self):
        print(self.internal_names)
        print(self.external_names)
        print(self.r)
        print(self.next)
        print(self.list)
        print(self.size)


if __name__ == '__main__':
    uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
    uf.union(1, 2).union(1, 3).print()
