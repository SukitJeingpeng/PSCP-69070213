"""PIG"""

N = int(input())
WEIGHTS = list(map(int, input().split()))

MAX_WEIGHTS = []
for i in range(0, N * 2, 2):
    MAX_WEIGHTS.append(max(WEIGHTS[i], WEIGHTS[i + 1]))

TOTAL = sum(MAX_WEIGHTS)
EQUATION = " + ".join(map(str, MAX_WEIGHTS))

if N == 1:
    print(TOTAL)
else:
    print(f"{EQUATION} = {TOTAL}")
