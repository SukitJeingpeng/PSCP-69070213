"""ISPRIME_LARGE"""

NUMBER = int(input())

if NUMBER <= 1:
    IS_PRIME = False
elif NUMBER == 2:
    IS_PRIME = True
elif not NUMBER % 2:
    IS_PRIME = False
else:
    IS_PRIME = True
    LIMIT = int(NUMBER**0.5)
    for DIVISOR in range(3, LIMIT + 1, 2):
        if not NUMBER % DIVISOR:
            IS_PRIME = False
            break

if IS_PRIME:
    print("YES")
else:
    print("NO")
