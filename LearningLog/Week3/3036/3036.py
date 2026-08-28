"""MAIN ข้อ ปราสาท"""

import math as m

N = int(input())

ALLROW = m.isqrt(N - 1) + 1
POSITION = N - (ALLROW - 1) ** 2

if POSITION % 2 == 1:
    print(2 * ALLROW - 2)
else:
    print(2 * ALLROW - 3)
