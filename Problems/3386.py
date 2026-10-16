"""DUPLICATE I"""

M = int(input())
N = int(input())

GROUP_1 = {input().strip() for _ in range(M)}
GROUP_2 = {input().strip() for _ in range(N)}

COMMON = sorted(GROUP_1 & GROUP_2, key=int, reverse=True)

if not COMMON:
    print("Nope")
else:
    for x in COMMON:
        print(x)
