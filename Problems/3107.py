"""MAIN"""

A,B,C = input().split()
B = int(B)
C = int(C)

if A == "M":
    if B < 5:
        TOTAL = C*0.06
    elif B > 10:
        TOTAL = C*0.10
    else:
        TOTAL = C*0.08
    TOTAL += 1500
elif A == "B":
    if B < 5:
        TOTAL = C*0.05
    elif B > 10:
        TOTAL = C*0.07
    else:
        TOTAL = C*0.06
    TOTAL += 1000
elif A == "G":
    if B < 5:
        TOTAL = C*0.04
    elif B > 10:
        TOTAL = C*0.06
    else:
        TOTAL = C*0.05
    TOTAL += 500

print(TOTAL)
