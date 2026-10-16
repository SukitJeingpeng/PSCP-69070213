"""Easy Histogram"""

N = int(input())
POLES = []

for _ in range(N):
    POLES.append(int(input()))

POLES.sort()

TOTAL = 0
CURRENT_DIST = 0
for HEIGHT in POLES:
    CURRENT_DIST += HEIGHT
    TOTAL += CURRENT_DIST * 2

print(TOTAL)
