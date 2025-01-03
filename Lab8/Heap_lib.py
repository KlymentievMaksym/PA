# а) Дослiдити особливостi реалiзацiї черги з прiоритетами стандартної бiблiотеки обраної
# мови програмування або однiєї з додаткових бiблiотек.
import heapq
h = []
d = [(1, 'd'), (3, 'e'), (2, 'f')]

heapq.heappush(h, (3, 'a'))
heapq.heappush(h, (2, 'b'))
heapq.heappush(h, (1, 'c'))
heapq.heappush(h, (4, 'd'))

heapq.heappush(d, (1, 'd'))
heapq.heappush(d, (3, 'e'))
heapq.heappush(d, (2, 'f'))

print(heapq.heappop(h))
heapq.merge(h, d)
print(h)

from heapq import heappop, heappush
h = []
heappush(h, (1, 'c'))

print(heappop(h))
print(heappop(h))