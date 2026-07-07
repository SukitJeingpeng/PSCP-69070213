'''MAIN'''

import math as m

A = float(input())
B = float(input())
C = float(input())
S = (A+B+C)/2
AREA = m.sqrt(S*(S-A)*(S-B)*(S-C))
print(f"{AREA:.3f}")
