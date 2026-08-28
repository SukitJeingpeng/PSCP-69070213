"""ภาษีรถยนต์"""

YEAR = int(input())
CC = int(input())

if YEAR <= 1990:
    if CC <= 1500:
        TAX = 1250
    elif CC <= 2000:
        TAX = 1400
    else:
        TAX = 2000

elif YEAR <= 1999:
    if CC <= 1500:
        TAX = 1100
    elif CC <= 2000:
        TAX = 1300
    else:
        TAX = 1700

else:
    if CC <= 1500:
        TAX = 1000
    elif CC <= 2000:
        TAX = 1200
    else:
        TAX = 1500

print(TAX)
