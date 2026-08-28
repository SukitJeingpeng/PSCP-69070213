"""MAIN"""

TOTAL = int(input())
THOUSAND = 0
FIVEHUNDRED = 0
HUNDRED = 0

if 20000 < TOTAL or TOTAL < 100:
    print("ERROR")
else:
    THOUSAND = TOTAL // 1000
    FIVEHUNDRED = (TOTAL - (THOUSAND * 1000)) // 500
    HUNDRED = (TOTAL - (THOUSAND * 1000 + FIVEHUNDRED * 500)) // 100
    TOTAL = TOTAL - (THOUSAND * 1000 + FIVEHUNDRED * 500 + HUNDRED * 100)
    if TOTAL:
        print("ERROR")
    else:
        if THOUSAND > 0:
            print(f"1000 = {THOUSAND}")
        if FIVEHUNDRED > 0:
            print(f"500 = {FIVEHUNDRED}")
        if HUNDRED > 0:
            print(f"100 = {HUNDRED}")
