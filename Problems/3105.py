"""MAIN"""

DISTANCE = int(input())
TOTAL = 35
NOW = 1

while NOW < DISTANCE:
    NOW += 1
    if NOW <= 10:
        TOTAL += 5
    elif NOW > 10:
        TOTAL += 8

if not DISTANCE:
    TOTAL = 0

print(TOTAL)
