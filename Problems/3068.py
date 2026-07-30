"""YEAR"""

YEAR = int(input())

if YEAR < 1582:
    if not YEAR % 4:
        print("yes")
    else:
        print("no")

else:
    if not YEAR % 400:
        print("yes")
    elif not YEAR % 100:
        print("no")
    elif not YEAR % 4:
        print("yes")
    else:
        print("no")
