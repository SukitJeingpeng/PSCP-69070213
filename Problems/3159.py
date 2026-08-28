"""FACTORIAL"""

NUMBER = int(input())
CALCULATE = 1

for i in range(NUMBER , 1 ,-1):
    CALCULATE *= i

print(CALCULATE)
