"""CAVE EXPLORER"""

N = int(input())
CAVE = list(map(int, input().split()))
COMMANDS = input().strip()

CODE_POS = CAVE.index(1)
CHEST_POS = CAVE.index(2)

for cmd in COMMANDS:
    if cmd == "R":
        if CODE_POS + 1 < N:
            CODE_POS += 1
    elif cmd == "L":
        if CODE_POS - 1 >= 0:
            CODE_POS -= 1

    if CODE_POS == CHEST_POS:
        break

FINAL_MAP = [0] * N
FINAL_MAP[CODE_POS] = 1

if CODE_POS != CHEST_POS:
    FINAL_MAP[CHEST_POS] = 2

print(*FINAL_MAP)
