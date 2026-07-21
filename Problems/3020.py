"""CocaCola MAIN"""

NORMALCOST = int(input())
BOTTLE_CAP = int(input())
SALECOST = int(input())
AMOUNT = int(input())

if BOTTLE_CAP == 0:
    CAL = AMOUNT * NORMALCOST
else:
    TOTALSALEAMOUNT = ((AMOUNT - 1) // BOTTLE_CAP)
    CAL = (NORMALCOST * (AMOUNT - TOTALSALEAMOUNT)) + (SALECOST * TOTALSALEAMOUNT)

print(CAL)
