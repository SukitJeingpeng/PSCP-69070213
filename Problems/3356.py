"""BUS SEAT"""

SEATS = int(input())
COLS = int(input())
TARGET = int(input())

for r in range(SEATS, 0, -1):
    ROW_SEATS = []
    for c in range(COLS):
        SEAT_NUM = c * SEATS + r
        if SEAT_NUM == TARGET:
            ROW_SEATS.append("XX")
        else:
            ROW_SEATS.append(f"{SEAT_NUM:02d}")
    print(*ROW_SEATS)
    if r % 2 and r > 1:
        print()
