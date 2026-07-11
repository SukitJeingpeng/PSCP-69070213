"""MAIN"""

X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    print("Q1")
elif Y > 0 > X:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
elif Y < 0 < X:
    print("Q4")
elif not X and not Y:
    print("O")
elif (X > 0 or X < 0) and not Y:
    print("X")
elif (Y > 0 or Y < 0) and not X:
    print("Y")
