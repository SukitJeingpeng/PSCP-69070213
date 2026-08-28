"""ZOOOOO"""

X,Y = input().split()
X = int(X)
TOTAL = 0

if X < 5:
    TOTAL = 0
elif X >= 19:
    TOTAL += 150
else:
    TOTAL += 100

if Y == "Wed":
    TOTAL /= 2

print(int(TOTAL))
