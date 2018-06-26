import random

import numpy as np

samples = np.random.normal(size=(4, 4))
# print(samples)

N = 10000000

# print(samples1)

position = 0
walk = [position]
steps = 10000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

# print(walk)
print(np.max(walk))
print(np.min(walk))
print((np.abs(walk) >= 10).argmax())



