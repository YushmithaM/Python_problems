import numpy as np
from itertools import repeat

Nums = [-1, 1, 0, -3, 3]
n = len(Nums)
prod = 1
res = []
for i in range(n):
    if Nums[i] == 0:
        index = i
        continue
    prod = prod * Nums[i]

for i in range(n):
    if Nums[i] == 0:
        res = list(repeat(0, n))
        res.insert(index, prod)
        break
    else:
        res.append(prod // Nums[i])

print(res)
