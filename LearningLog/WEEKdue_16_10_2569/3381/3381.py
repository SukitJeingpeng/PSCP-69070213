"""POINT SORTING"""

T = int(input())

for _ in range(T):
    N = int(input())
    POINTS = []
    for _ in range(N):
        X, Y = map(int, input().split())
        POINTS.append([X, Y])
    POINTS.sort(key=lambda pt: (pt[0] + pt[1], -pt[1]))
    for x, y in POINTS:
        print(f"{x} {y}")
