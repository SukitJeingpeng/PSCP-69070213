"""MAIN"""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

total_items = a + b + c
total_price = (a * 25) + (b * 40) + (c * 55)

if total_items >= 3:
    total_price -= total_price * 0.1

print(int(total_price))
