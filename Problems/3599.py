"""NUMBERPLUSPLUS"""

NEED = int(input())
TOTAL = 0
while True:
    i = int(input())
    if i != -1 and TOTAL != NEED:
        TOTAL += i
    else:
        break

print(TOTAL)
