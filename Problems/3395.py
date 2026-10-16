"""RESTAURANT QUEUE"""

N = int(input().split()[0])
HEIGHTS = list(map(int, input().split()))
CUSTOMERS = list(map(int, input().split()))

PREFIX_MAX = [0] * N
CURRENT_MAX = 0

for i in range(N):
    PREFIX_MAX[i] = CURRENT_MAX
    if HEIGHTS[i] > CURRENT_MAX:
        CURRENT_MAX = HEIGHTS[i]

for pos in CUSTOMERS:
    idx = pos - 1
    MAX_FRONT = PREFIX_MAX[idx]
    CHAIR = MAX_FRONT - HEIGHTS[idx] + 1
    if CHAIR < 0:
        CHAIR = 0
    print(CHAIR)
