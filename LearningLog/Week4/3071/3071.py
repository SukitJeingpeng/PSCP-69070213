"""Remain"""

NUM1 = int(input())
NUM2 = int(input())
DIVIDE = int(input())
REMAIN = int(input())
SCORE = 0

for i in range(NUM1,NUM2+1):
    if i % DIVIDE == REMAIN:
        SCORE += 1

print(SCORE)
