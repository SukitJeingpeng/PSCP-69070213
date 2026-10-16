"""FAIFARR"""
UNITS = int(input())
NOW = UNITS
TOTAL = 0

if NOW > 200:
    TOTAL += (NOW - 200) * 15
    NOW = 200
if NOW > 100:
    TOTAL += (NOW - 100) * 12
    NOW = 100
if NOW > 50:
    TOTAL += (NOW - 50) * 10
    NOW = 50
if NOW > 10:
    TOTAL += (NOW - 10) * 7
    NOW = 10
if NOW > 0:
    TOTAL += NOW * 5
FINAl = (TOTAL * 1.07) + (UNITS * 0.5)
print(f"{FINAl:.1f}")
