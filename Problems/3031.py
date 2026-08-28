"""Ink"""
import math as m

S, N = input().split()
S = int(S)
N = int(N)
PIE = 3.1416
for _ in range(N):
    X, Y = input().split()
    X = float(X)
    Y = float(Y)
    TIME = (PIE * (X**2 + Y**2)) / S
    print(m.ceil(TIME))
