"""ARRAY 2D CHECK"""

GRID = [list(map(int, input().split())) for _ in range(5)]

BAD_ROW = -1
BAD_COL = -1

for r in range(5):
    if sum(GRID[r]) % 2:
        BAD_ROW = r

for c in range(5):
    COL_SUM = sum(GRID[r][c] for r in range(5))
    if COL_SUM % 2:
        BAD_COL = c

print(f"{BAD_ROW} {BAD_COL}")
