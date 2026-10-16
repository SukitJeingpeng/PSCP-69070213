"""PUT IT IN THE BOX !"""

NUMBER = input().split()

W = int(NUMBER[0])
L = int(NUMBER[1])
M = int(NUMBER[2])
N = int(NUMBER[3])

MIN = float("inf")

for A in range(M, N + 1):
    WASTE = (W % A) * (L % A)

    if WASTE < MIN:
        MIN = WASTE

print(MIN)
