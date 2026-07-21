"""ข้อสอบกระต่าย MAIN"""

RABBIT = int(input())
SCORE = []
TOPSTUDENT = 0

for i in range(RABBIT):
    i = input()
    SCORE.append(i)

BEST = SCORE[0]

for j in range(RABBIT):
    if j < RABBIT:
        if int(SCORE[j]) > int(BEST):
            BEST = SCORE[j]
    else:
        break

for k in SCORE:
    if BEST == k:
        TOPSTUDENT += 1

print(BEST)
print(TOPSTUDENT)
