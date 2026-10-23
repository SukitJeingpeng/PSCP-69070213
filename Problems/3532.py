"""GCD_V2"""

A_INPUT = input().strip()
B_INPUT = input().strip()

if "." in A_INPUT:
    A = int(float(A_INPUT))
else:
    A = int(A_INPUT)

if "." in B_INPUT:
    B = int(float(B_INPUT))
else:
    B = int(B_INPUT)

while B:
    REMAINDER = A % B
    A = B
    B = REMAINDER

print(abs(A))
