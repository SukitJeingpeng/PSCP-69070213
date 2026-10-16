"""113"""

TEXT = input()
STACK = []

for c in TEXT:
    STACK.append(c)
    if STACK[-3:] == ["1", "1", "3"]:
        del STACK[-3:]

print("".join(STACK))
