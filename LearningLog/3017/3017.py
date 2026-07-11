'''MAIN'''

COST = float(input())
SERVICE = COST * 0.1

if SERVICE <= 50:
    SERVICE = 50

if SERVICE >= 1000:
    SERVICE = 1000

VATPLUS =  (COST + SERVICE) *0.07
print(f"{(COST + SERVICE + VATPLUS):.2f}")
