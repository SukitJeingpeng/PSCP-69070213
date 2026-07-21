"""ตัวเลขน้อยสุด"""
LISTNUMBER = []

for i in range(3):
    i = int(input())
    LISTNUMBER.append(i)

LOWEST = LISTNUMBER[0]

for i in range(3):
    if LISTNUMBER[i] < LOWEST:
        LOWEST = LISTNUMBER[i]

print(LOWEST)
