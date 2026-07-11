"""MAIN"""

NUM1 = input()
OPERATE = input()
NUM2 = NUM1[::-1]
NUM1 = int(NUM1)
NUM2 = int(NUM2)

if OPERATE == "+":
    print(f"{NUM1} + {NUM2} = {NUM1 + NUM2}")

else:
    print(f"{NUM1} * {NUM2} = {NUM1 * NUM2}")
