'''main'''

X = int(input())
Y = int(input())
A = int(input())
Z = int(input())
TOTAL = 0

if X > Y:
    TOTALP = (Z // X)*(X-Y)
    TOTAL = (Z*A)-(A*TOTALP)

print(TOTAL)
