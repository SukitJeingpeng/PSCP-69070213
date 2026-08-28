"""MAIN"""

S,R = input().split()
N = input().split()
O = 0

for i in range(len(N)):
    if i > 0:
        O = int(N[1])
        N = N[0]

TOTAL = 0

if S == "S":
    TOTAL += 60
elif S == "M":
    TOTAL += 80
elif S == "L":
    TOTAL += 100

if R == "T":
    TOTAL += 20

if N == "P":
    TOTAL += 15 * O
elif N == "E":
    TOTAL += 10 * O

print(TOTAL)
