"""BUS STOP I"""

P = int(input())
N = int(input())

STOPS = {}
for _ in range(N):
    PARTS = list(map(int, input().split()))
    STOPS[PARTS[0]] = PARTS[1:]

BUS = []
ARRIVED = 0

for s in range(1, N + 1):
    NEW_BUS = []
    for d in BUS:
        if d == s:
            ARRIVED += 1
        else:
            NEW_BUS.append(d)
    BUS = NEW_BUS

    if s in STOPS:
        for d in STOPS[s]:
            if len(BUS) == P:
                break
            if d > s:
                BUS.append(d)

print(ARRIVED)
