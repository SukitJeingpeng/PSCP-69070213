"""FLOWERS"""

import math as m
L, N = input().split()
L = int(L)
N = int(N)
NOW = 1
FLOOR = 0
TIMES = 1
while NOW <= N:
    NOW += TIMES
    TIMES += 1
    FLOOR += 1
print(m.ceil(FLOOR / L))