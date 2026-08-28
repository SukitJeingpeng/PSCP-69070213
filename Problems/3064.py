"""BIRTHDAY"""
from datetime import date

YEAR1 = int(input())
MONTH1 = int(input())
DAY1 = int(input())
YEAR2 = int(input())
MONTH2 = int(input())
DAY2 = int(input())
D1 = date(YEAR1, MONTH1, DAY1)
D2 = date(YEAR2, MONTH2, DAY2)
DIFF = abs((D1 - D2).days)

if DIFF <= 7:
    print(0)
elif D1 < D2:
    print(1)
else:
    print(2)
