"""BIRTHDAY"""

YEAR1 = int(input())
MONTH1 = int(input())
DAY1 = int(input())
YEAR2 = int(input())
MONTH2 = int(input())
DAY2 = int(input())

if YEAR1 == YEAR2:
    if MONTH1 == MONTH2:
        if DAY1 - DAY2 or DAY2 - DAY1 <=7:
            print("0")
        elif DAY1 > DAY2:
            print("1")
        elif DAY2 > DAY1:
            print("2")
    elif MONTH1 > MONTH2:
        print("1")
    elif MONTH2 > MONTH1:
        print("2")
elif YEAR1 > YEAR2:
    print("1")
elif YEAR2 > YEAR1:
    print("2")
