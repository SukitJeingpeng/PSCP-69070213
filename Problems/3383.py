"""DIFFERENCE"""

N = int(input())
M = int(input())

SET_A = {int(input()) for _ in range(N)}
SET_B = {int(input()) for _ in range(M)}

DIFF = SET_A - SET_B
print(*sorted(DIFF))
