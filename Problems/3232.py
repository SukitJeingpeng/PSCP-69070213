"""JUMPING FROG"""

X,Y = input().split()
X = int(X)
Y = int(Y)
COUNT = 0
ERROR = False

while Y > 0:
    if X <= 0:
        ERROR = True
        break
    COUNT += 1
    Y -= X
    X -= 2

if ERROR is True:
    print("-1")
else:
    print(COUNT)
