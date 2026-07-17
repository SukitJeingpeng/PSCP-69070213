"""MAIN"""

NUMBER = int(input())
LISTNUMBER = []

for i in range(NUMBER+1):
    if i % 10 == 0:
        LISTNUMBER.append(i)

print(str(LISTNUMBER))