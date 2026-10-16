"""RAILWAY LIGHT"""

N = int(input())
TRACK = [False] * 360

for _ in range(N):
    A, B = map(int, input().split())
    if A < B:
        for i in range(A, B):
            TRACK[i] = True
    else:
        for i in range(A, 360):
            TRACK[i] = True
        for i in range(0, B):
            TRACK[i] = True

if all(TRACK):
    print(360)
else:
    DOUBLE_TRACK = TRACK * 2
    MAX_LIGHT = 0
    CURRENT = 0
    for LIGHT in DOUBLE_TRACK:
        if LIGHT:
            CURRENT += 1
            if CURRENT > MAX_LIGHT:
                MAX_LIGHT = CURRENT
        else:
            CURRENT = 0
    print(MAX_LIGHT)
