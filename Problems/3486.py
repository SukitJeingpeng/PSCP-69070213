"""ARTILLERY TARGET"""

N = int(input())
SHOTS = []

for _ in range(N):
    X, Y, D = map(int, input().split())
    SHOTS.append((X, Y, D))

X1, Y1, D1 = SHOTS[0]
FOUND = False

for dx in range(-D1, D1 + 1):
    REM = D1 * D1 - dx * dx
    dy = int(REM ** 0.5)
    if dy * dy == REM:
        for sign in (1, -1):
            TX = X1 + dx
            TY = Y1 + sign * dy
            VALID = True
            for xj, yj, dj in SHOTS:
                if (TX - xj) ** 2 + (TY - yj) ** 2 != dj * dj:
                    VALID = False
                    break
            if VALID:
                print(f"{TX} {TY}")
                FOUND = True
                break
    if FOUND:
        break
