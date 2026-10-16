"""CAL"""

CAL = 0

while True:
    NUM = int(input())
    if NUM != 5:
        if NUM == 1:
            CAL += 100
        elif NUM == 2:
            CAL += 120
        elif NUM == 3:
            CAL += 200
        elif NUM == 4:
            CAL += 60
    else:
        break

print("Bye Bye")
print(f"Total Calories: {CAL}")
