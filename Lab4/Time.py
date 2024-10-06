from KruskalsAlgorithm import KruskalsAlgorithm

import time
import numpy as np
import matplotlib.pyplot as plt

sizes = [number for number in range(10, 400, 50)]
times = []
for size in sizes:
    kruskal_times = []
    print(size)
    for _ in range(100):
        kruskal = KruskalsAlgorithm(size)
        start = time.time()
        kruskal.start()
        end = time.time()
        kruskal_times.append(end - start)
    times.append(np.mean(kruskal_times))

plt.plot(sizes, times, label="Kruskal")
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()
