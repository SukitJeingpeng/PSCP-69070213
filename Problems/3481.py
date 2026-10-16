"""ลอดสะพาน"""

L, N = map(int, input().split())

DIFF = [0] * (L + 1)

for _ in range(N):
    A, B = map(int, input().split())
    DIFF[A] += 1
    DIFF[B] -= 1

MAX_BRIDGES = 0
CURR = 0

for i in range(L):
    CURR += DIFF[i]
    if CURR > MAX_BRIDGES:
        MAX_BRIDGES = CURR

print(MAX_BRIDGES)
