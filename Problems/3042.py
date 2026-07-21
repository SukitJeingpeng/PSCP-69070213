"""MAIN"""

NUMBER = int(input())
LISTNUMBER = []

for i in range(NUMBER+1):
    if not i % 10:
        LISTNUMBER.append(i)
        
print(*LISTNUMBER[::-1])
