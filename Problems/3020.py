"""CocaCola MAIN"""

NORMALCOST = int(input())
BOTTLE_CAP = int(input())
SALECOST = int(input())
AMOUNT = int(input())

if not AMOUNT:
    CAL = 0
elif not BOTTLE_CAP:
    CAL = NORMALCOST * AMOUNT
else:
    DISCOUNTED = (AMOUNT - 1) // BOTTLE_CAP
    CAL = NORMALCOST * (AMOUNT - DISCOUNTED) + SALECOST * DISCOUNTED

print(CAL)
