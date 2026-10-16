"""RARE ARTIFACTS"""

input()
CODES = list(map(int, input().split()))

COUNT = {}
for code in CODES:
    if code in COUNT:
        COUNT[code] += 1
    else:
        COUNT[code] = 1

UNIQUE = []
for code, cnt in COUNT.items():
    if cnt == 1:
        UNIQUE.append(code)

UNIQUE.sort()
print(*UNIQUE)
