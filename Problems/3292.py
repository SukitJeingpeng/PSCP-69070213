"""LEFT RIGHT ARROW"""

RL = input()
READ = int(input())

for i, CHECK in enumerate(RL):
    for ROW in range(READ * 2 - 1):
        if CHECK == "R":
            if ROW < READ:
                print(" " * (ROW * 2) + "*" * (READ - ROW))
            else:
                print(" " * ((READ * 2 - 2 - ROW) * 2) + "*" * (ROW - READ + 2))
        elif CHECK == "L":
            if ROW < READ:
                print(" " * (READ - ROW - 1) + "*" * (READ - ROW))
            else:
                print(" " * (ROW - READ + 1) + "*" * (ROW - READ + 2))

    if i != len(RL) - 1:
        print()
