"""CARS"""

N = int(input())
V_LIST = [int(input().split()[1]) for _ in range(N)]

UNSOLD = 0
MAX_V = 0

for i in range(N - 1, -1, -1):
    if V_LIST[i] < MAX_V:
        UNSOLD += 1
    else:
        MAX_V = V_LIST[i]

print(UNSOLD)
