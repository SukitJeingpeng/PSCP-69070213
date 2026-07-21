"""MAIN ข้อ ต่อแถว"""

PEOPLE, ROW = input().split()
PEOPLE, ROW = int(PEOPLE), int(ROW)

PEOPLELIST = []
PEOPLEINROW = 0

count = [0] * (ROW + 1)

for i in range(PEOPLE):
    i = int(input())
    PEOPLELIST.append(i)

for j in PEOPLELIST:
    count[j] += 1

TRAIN = min(count[1:])

TOTALLEFT = PEOPLE - (TRAIN * ROW)

print(TOTALLEFT)
