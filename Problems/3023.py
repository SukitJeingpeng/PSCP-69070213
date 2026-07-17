"""MAIN"""
NUMBER = int(input())
COUNT = 0
POINT = 0

while True:
    if POINT < NUMBER:
        POINT += 1
        COUNT += int(len(str(POINT))) + 1
    else:
        break

if NUMBER == 1:
    COUNT = 1

print(COUNT)
