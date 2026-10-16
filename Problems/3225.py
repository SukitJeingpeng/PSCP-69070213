"""FAT RABBIT"""

NUM = int(input())
RABBITNAME = []
RABBITWEIGHT = []
FATCOUNT = 0
FATTEST = ""

for _ in range(NUM):
    NAME, WEIGHT = input().split()
    WEIGHT = int(WEIGHT)
    RABBITNAME.append(NAME)
    RABBITWEIGHT.append(WEIGHT)

MAXWEIGHT = max(RABBITWEIGHT)
for i, WEIGHT in enumerate(RABBITWEIGHT):
    if WEIGHT > 15:
        FATCOUNT += 1
    if WEIGHT == MAXWEIGHT:
        FATTEST = RABBITNAME[i]

print(FATCOUNT)
print(FATTEST)
