# б ) Пiдготувати данi рiзного розмiру для проведення порiвняльного аналiзу. Мають бути
# набори повнiстю вiдсортованi данi, випадковi, майже вiдсортованi, вiдсортованi в
# зворотному порядку та лише з декiлькома рiзними значеннями всiх розмiрiв. Розмiр
# даних має бути з достатнього дiапазону, щоб побачити тенденцiю, й повинен мiстити
# такi, на яких можна побачити рiзницю. Можна взяти обмеження за часом виконання вiд
# 0.01с до 30с.


from numpy import random


class RandomLists:
    def __init__(self, n: int, type: str, *args):
        self._TYPES = {'sorted': self.sorted, 'random': self.random, 'almostsorted': self.almostsorted, 'reverse': self.reverse, 'somenumbers': self.somenumbers}
        self.n = n
        if type not in self._TYPES:
            raise ValueError(f'Invalid type: {type}')
        self.list = self._TYPES[type](*args)
    
    def sorted(self):
        random_start = random.randint(0, self.n)
        random_step = random.randint(0, self.n)
        n = 0
        to_return = []
        while n != self.n:
            to_return.append(random_start)
            random_start += random_step
            n += 1
        return to_return

    def random(self):
        return list(random.randint(0, self.n, self.n))

    def almostsorted(self):
        raise NotImplementedError

    def reverse(self):
        return self.sorted()[::-1]

    def somenumbers(self, range_start=1, range_end=5):
        random_start = random.randint(0, self.n)
        random_step = random.randint(range_start, range_end)
        return list(random.randint(random_start, random_start + random_step, self.n))

    def __str__(self):
        return str(self.list)

if __name__ == '__main__':
    rng = RandomLists(10, 'somenumbers')
    print(rng)
