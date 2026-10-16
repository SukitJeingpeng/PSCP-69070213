"""GIRAFFE"""

N = int(input())
HEIGHTS = [int(input()) for _ in range(N)]

COUNT = 0
for i in range(N):
    PEAK = True
    if i > 0 and HEIGHTS[i] < HEIGHTS[i - 1]:
        PEAK = False
    if i < N - 1 and HEIGHTS[i] < HEIGHTS[i + 1]:
        PEAK = False
    if PEAK:
        COUNT += 1

print(COUNT)
