"""MAIN ห่อของขวัญ"""

RADIUS, HEIGHT, GLUE = input().split()
RADIUS, HEIGHT, GLUE = float(RADIUS), float(HEIGHT), float(GLUE)

PI = 3.14

LONG = (2*PI*RADIUS) + GLUE
WIDE = (2*RADIUS) + HEIGHT

print(f"{WIDE:.2f} {LONG:.2f}")
