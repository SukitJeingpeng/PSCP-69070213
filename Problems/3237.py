"""รหัส Triangle """

ACTION = int(input())

for i in range(1,ACTION+1):
    for j in range(1,i+1):
        if i == j or j == 1 or i == ACTION:
            print("0", end="")
        else:
            print("1", end="")
    print()
