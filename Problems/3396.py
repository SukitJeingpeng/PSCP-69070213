"""แซงรอบ"""

N, K = map(int, input().split())
TIMES = [int(input()) for _ in range(N)]

S_MIN = min(TIMES)
TARGET = K * S_MIN
SURVIVORS = 0

for s in TIMES:
    if (K - 1) * s < TARGET:
        SURVIVORS += 1

print(SURVIVORS)
