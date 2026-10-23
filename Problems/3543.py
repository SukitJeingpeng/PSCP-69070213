"""SIEVE OF ERATOSTHENES"""

N = int(input())

if N <= 1:
    print("No")
else:
    IS_PRIME = [True] * (N + 1)
    IS_PRIME[0] = False
    IS_PRIME[1] = False

    LIMIT = int(N**0.5)
    for p in range(2, LIMIT + 1):
        if IS_PRIME[p]:
            for multiple in range(p * p, N + 1, p):
                IS_PRIME[multiple] = False

    if IS_PRIME[N]:
        print("Yes")
        PRIMES = []
        for number in range(2, N + 1):
            if IS_PRIME[number]:
                PRIMES.append(number)
        print(*PRIMES)
    else:
        print("No")
