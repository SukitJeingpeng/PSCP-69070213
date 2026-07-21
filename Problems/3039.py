"""ตัวเลขน้อยสุด"""

N = int(input())
NUMBER = []

for i in range(N):
    i = int(input())
    NUMBER.append(i)

LOWEST = NUMBER[0]

for j in range(N):
    if NUMBER[j] < LOWEST:
        LOWEST = NUMBER[j]

print(LOWEST)
