"""ตัวเลขมากสุด"""
LISTNUMBER = []

for i in range(3):
    i = int(input())
    LISTNUMBER.append(i)

HIGHEST = LISTNUMBER[0]

for i in range(3):
    if LISTNUMBER[i] > HIGHEST:
        HIGHEST = LISTNUMBER[i]

print(HIGHEST)
