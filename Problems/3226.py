"""MAIN"""

from decimal import Decimal, ROUND_DOWN

money = Decimal(input())
years = int(input())
rate = Decimal("0.0381")
cent = Decimal("0.01")

for _ in range(years):
    increase = (money * rate).quantize(cent, rounding=ROUND_DOWN)
    money += increase

print(f"{money:.2f}")
