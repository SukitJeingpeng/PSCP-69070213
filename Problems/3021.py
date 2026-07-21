"""OverlapCircle"""
import math as m

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

Calculate = m.sqrt((x2-x1)**2 + (y2-y1)**2)
if Calculate < r1+r2:
    print("overlapping")
elif Calculate > r1+r2:
    print("no overlapping")
