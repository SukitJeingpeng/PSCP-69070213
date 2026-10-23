"""MissingNumber"""
TARGET = int(input())
NUMBLIST = []
TARGETLIST = []
while True:
    i = int(input())
    if i:
        NUMBLIST.append(i)
    else:
        break

for i in range(1, TARGET+1):
    TARGETLIST.append(i)

NUMBLIST.sort(reverse=False)
TARGETLIST.sort(reverse=False)

for j in range(TARGET):
    if TARGETLIST[j] not in NUMBLIST:
        print(TARGETLIST[j])
