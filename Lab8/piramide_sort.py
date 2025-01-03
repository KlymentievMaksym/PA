# б ) Реалiзувати алгоритм пiрамiдального сортування та продемонструвати його роботу з
# даними рiзного розмiру.

class PiramideSort:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array

    def _swap(self, index_from: int, index_to: int) -> None:
        self.array[index_from], self.array[index_to] = self.array[index_to], self.array[index_from]

    def _sift_up(self, index: int) -> None:
        parent = (index-1)//2
        if parent != -1:
            if self.array[index] < self.array[parent]:
                self._swap(index, parent)
                self._sift_up(parent)

    def _sift_down(self, index: int) -> None:
        child_left = 2*index + 1
        child_right = 2*index + 2
        if child_right < len(self.array):
            if self.array[child_left] <= self.array[child_right]:
                if self.array[index] > self.array[child_left]:
                    self._swap(index, child_left)
                    self._sift_down(child_left)
                elif self.array[index] > self.array[child_right]:
                    self._swap(index, child_right)
                    self._sift_down(child_right)
            else:
                if self.array[index] > self.array[child_right]:
                    self._swap(index, child_right)
                    self._sift_down(child_right)
                elif self.array[index] > self.array[child_left]:
                    self._swap(index, child_left)
                    self._sift_down(child_left)

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

    def peek(self):
        raise NotImplementedError

    def heapify(self):
        raise NotImplementedError

    def search(self, value: int):
        raise NotImplementedError

    def extract_max(self):
        raise NotImplementedError

    def extract_min(self):
        raise NotImplementedError

    def update(self, index: int, value: int):
        raise NotImplementedError

    def __repr__(self):
        return str(self.array)


if __name__ == '__main__':
    ps = PiramideSort()
    ps.insert(109)
    ps.insert(3)
    ps.insert(5)
    ps.insert(2)
    # ps.insert(1)
    print(ps)
    print(ps.delete())
    print(ps)
    print(ps.delete())
    print(ps)
    print(ps.delete())
    print(ps)
    print(ps.delete())
    print(ps)
    # print(ps.delete())
    # print(ps)
