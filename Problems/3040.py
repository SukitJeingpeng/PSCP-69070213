"""MAIN แลกเปลี่ยนเงิน"""

MONEY = int(input())

TEN = MONEY // 10
MONEY -= TEN * 10

FIVE = MONEY // 5
MONEY -= FIVE * 5

TWO = MONEY // 2
MONEY -= TWO * 2

ONE = MONEY

print(f"10 = {TEN}")
print(f"5 = {FIVE}")
print(f"2 = {TWO}")
print(f"1 = {ONE}")
