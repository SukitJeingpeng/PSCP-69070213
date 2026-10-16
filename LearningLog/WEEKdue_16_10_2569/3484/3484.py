"""หุ่นยนต์เคาะเสียงกระเบื้อง"""

FIRST = input().split()
N = int(FIRST[0])
P = float(FIRST[1])

GRID = []
for _ in range(N):
    ROW = [int(val) for val in input().split()]
    GRID.append(ROW)

for r in range(N):
    ROLLDEFLECT = 0
    ROLLDEFLECTPOINTS = 0
    for val in GRID[r]:
        if val > 0:
            ROLLDEFLECT += 1
        ROLLDEFLECTPOINTS += val
    print(*GRID[r], ROLLDEFLECT, ROLLDEFLECTPOINTS)

COLDEFECT = []
COLDEFPOINTS = []

for c in range(N):
    TILES = 0
    TILESPOINTS = 0
    for r in range(N):
        val = GRID[r][c]
        if val > 0:
            TILES += 1
        TILESPOINTS += val
    COLDEFECT.append(TILES)
    COLDEFPOINTS.append(TILESPOINTS)

print(*COLDEFECT)
print(*COLDEFPOINTS)

TOTALTILES = sum(COLDEFECT)
TOTALPOINTS = sum(COLDEFPOINTS)
FINE = TOTALPOINTS * P

print(f"{TOTALTILES} {TOTALPOINTS} {FINE:.2f}")
