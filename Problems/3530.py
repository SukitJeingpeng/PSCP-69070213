"""SQFREE"""

N = int(input())

IS_SQUARE_FREE = [True] * (N + 1)
MAX_B = int(N**0.5)

for i in range(2, MAX_B + 1):
    SQUARE = i * i
    for j in range(SQUARE, N + 1, SQUARE):
        IS_SQUARE_FREE[j] = False

COUNT = 0
for k in range(1, N + 1):
    if IS_SQUARE_FREE[k]:
        COUNT += 1

print(COUNT)
