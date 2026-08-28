"""MAIN MILKKK"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

TOTAL = d // a
TOTALBOTTLE = TOTAL

if b > 0:
    while TOTAL >= b:
        TOTAL = TOTAL - b
        TOTAL += c
        TOTALBOTTLE += c

print(TOTALBOTTLE)
