'''main'''

X = float(input())
Y = float(input())
A = float(input())
Z = float(input())

DISCOUNT = (Z // X) * (X-Y)
TOTAL = (Z-DISCOUNT)*A

print(round(TOTAL))
