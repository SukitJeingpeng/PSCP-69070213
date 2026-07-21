"""AR TKTOK"""

R, X, Y = input().split()
R, X, Y = int(R), int(X), int(Y)

if R**2 > X**2+Y**2:
    print("IN")
elif R**2 == X**2+Y**2:
    print("ON")
else:
    print("OUT")
