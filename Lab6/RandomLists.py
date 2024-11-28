# б ) Пiдготувати данi рiзного розмiру для проведення порiвняльного аналiзу. Мають бути
# набори повнiстю вiдсортованi данi, випадковi, майже вiдсортованi, вiдсортованi в
# зворотному порядку та лише з декiлькома рiзними значеннями всiх розмiрiв. Розмiр
# даних має бути з достатнього дiапазону, щоб побачити тенденцiю, й повинен мiстити
# такi, на яких можна побачити рiзницю. Можна взяти обмеження за часом виконання вiд
# 0.01с до 30с.


from Converter import Converter
from numpy import random


class RandomLists:
    def __init__(self, n: int, type: str, *args, **kwargs):
        self._TYPES = {'sorted': self.sorted, 'random': self.random, 'almostsorted': self.almostsorted, 'reverse': self.reverse, 'somenumbers': self.somenumbers}
        if type not in self._TYPES:
            raise ValueError(f'Invalid type: {type}, excpected one of {list(self._TYPES.keys())}')

        self.n = n
        if self.n <= 0:
            raise ValueError(f'Invalid n: {self.n}, expected positive integer')

        linked_list = kwargs.get('linked_list', False)
        linked_list = kwargs.get('linlist', linked_list)
        linked_list = kwargs.get('llist', linked_list)

        self.list = self._TYPES[type](*args, **kwargs)
        if linked_list:
            self.list = Converter.array_to_linked_list(self.list)
    
    def sorted(self, *args, **kwargs):
        start = kwargs.get('start', 0)
        random_start = random.randint(start, self.n)
        random_step = random.randint(start, self.n)
        n = 0
        to_return = []
        while n != self.n:
            to_return.append(random_start)
            random_start += random_step
            n += 1
        return to_return

    def random(self, *args, **kwargs):
        return list(random.randint(0, self.n, self.n))

    def almostsorted(self, disorder_level: float = 0.05, *args, **kwargs):
        to_return = self.sorted(*args, **kwargs)

        num_swaps = int(disorder_level * self.n)

        for _ in range(num_swaps):
            i, j = random.randint(0, self.n-1), random.randint(0, self.n-1)
            to_return[i], to_return[j] = to_return[j], to_return[i]
        return to_return

    def reverse(self, *args, **kwargs):
        return self.sorted(*args, **kwargs)[::-1]

    def somenumbers(self, range_start=1, range_end=5, *args, **kwargs):
        random_start = random.randint(0, self.n)
        random_step = random.randint(range_start, range_end)
        return list(random.randint(random_start, random_start + random_step, self.n))

    def triangular(self, *args, **kwargs):
        sorted = self.sorted(*args, **kwargs)
        reversed = sorted[::-1]
        return sorted[:self.n//2] + reversed[self.n//2:]

    def __str__(self):
        return str(self.list)

if __name__ == '__main__':
    rng = RandomLists(10, 'almostsorted', linked_list=True)
    print(rng)
