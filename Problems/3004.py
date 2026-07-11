"""main"""
import math as m

A = input().split()
X1 = int(A[0])
Y1 = int(A[1])
Z1 = int(A[2])

B = input().split()
X2 = int(B[0])
Y2 = int(B[1])
Z2 = int(B[2])

X = X1 - X2
Y = Y1 - Y2
Z = Z1 - Z2

print(f"{m.sqrt(X**2 + Y**2 + Z**2):.2f}")
