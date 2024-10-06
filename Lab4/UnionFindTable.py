class UnionFindTable:
    def __init__(self, sets=[]):
        while [] in sets:
            sets.remove([])

        len_of_sets = len(sets)
        size_of_sets = 0

        for set in sets:
            # size_of_sets += len(set)
            size_of_sets = max(size_of_sets, max(set))

        self.r = [0] * size_of_sets
        self.list = [0] * len_of_sets
        self.next = [0] * size_of_sets
        self.size = [0] * len_of_sets
        self.internal_names = {internal_name+1: len_of_sets-1-internal_name for internal_name in range(len_of_sets)}
        self.external_names = {external_name: len_of_sets-external_name for external_name in range(len_of_sets-1, -1, -1)}
        for single_set in sets:
            index = self.internal_names[sets.index(single_set)+1]
            for item in single_set:
                self.r[item-1] = index
                next_item = single_set.index(item)+1
                if next_item < len(single_set):
                    self.next[item-1] = single_set[next_item]
                self.size[index] = len(single_set)
            self.list[index] = single_set[0]

    def make_sets(self):
        values_used = []
        sets = []
        for key, value in self.internal_names.items():
            single_set = []
            if value not in values_used:
                values_used.append(value)
                number = self.list[value]
                k = 0
                while number != 0:
                    # print(number, k)
                    if number == self.next[self.list[value]-1]:
                        k += 1
                        if k >= 2:
                            print('Break because loop is happening...')
                            break
                    single_set.append(number)
                    number = self.next[number-1]
                # print(number, k)
            sets.append(single_set)
        return sets

    def find(self, x):
        return self.external_names[self.r[x-1]]

    def union(self, x, y):
        A = self.internal_names[x]
        B = self.internal_names[y]
        if A == B:
            return self
        if self.size[A] > self.size[B]:
            A, B = B, A
            x, y = y, x
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

    def print(self):  # pragma: no cover
        print('Internal names:', self.internal_names)
        print('External names:', self.external_names)
        print('List of r:', self.r)
        print('List of next:', self.next)
        print('List of first elements:', self.list)
        print('Sizes:', self.size)
        print('Current sets:', self.make_sets())
        return self


if __name__ == '__main__':  # pragma: no cover
    uf = UnionFindTable([[1, 3, 5, 7], [2, 4, 8], [6]])
    uf.print()
    uf.union(1, 2).print()
    # uf.print()
    # uf = UnionFindTable(uf.make_sets())
    # uf.union(1, 2)
    uf.union(1, 3)
    uf.print()
