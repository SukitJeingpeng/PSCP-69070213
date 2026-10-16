"""Inflation"""
MONEY = int(float(input()) * 100)
YEARS = int(input())

for _ in range(YEARS):
    MONEY = MONEY * 10381 // 10000

INCREASE = MONEY // 100
TODSANHIYOM = MONEY % 100
print(f"{INCREASE}.{TODSANHIYOM:02d}")
