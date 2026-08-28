"""RECTANGLE AREA"""

REC1 = input()
REC2 = input()

X1,Y1,LONG1,HEIGHT1 = REC1.split()
X2,Y2,LONG2,HEIGHT2 = REC2.split()

X1 = int(X1)
Y1 = int(Y1)
LONG1 = int(LONG1)
HEIGHT1 = int(HEIGHT1)

X2 = int(X2)
Y2 = int(Y2)
LONG2 = int(LONG2)
HEIGHT2 = int(HEIGHT2)

LEFT1 = X1
RIGHT1 = X1 + LONG1
BOTTOM1 = Y1
TOP1 = Y1 + HEIGHT1

LEFT2 = X2
RIGHT2 = X2 + LONG2
BOTTOM2 = Y2
TOP2 = Y2 + HEIGHT2

OVER_W = min(RIGHT2, RIGHT1) - max(LEFT1, LEFT2)
OVER_H = min(TOP1, TOP2) - max(BOTTOM1, BOTTOM2)

if OVER_H > 0 and OVER_W > 0:
    AREA = OVER_H * OVER_W
    print(AREA)
else:
    print("no overlapping")
