"""ODD or EVEN"""

NUM1 = int(input())
NUM2 = int(input())
NUM3 = int(input())
ODD = 0
EVEN = 0

if NUM1 % 2 == 1:
    ODD += 1
else:
    EVEN += 1

if NUM2 % 2 == 1:
    ODD += 1
else:
    EVEN += 1

if NUM3 % 2 == 1:
    ODD += 1
else:
    EVEN += 1

print(EVEN)
print(ODD)
