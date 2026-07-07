'''main'''

COLOR1 = input().lower()
COLOR2 = input().lower()

if (COLOR1 == "yellow" and COLOR2 == "red") or (COLOR1 == "red" and COLOR2 == "yellow"):
    print("Orange")
elif (COLOR1 == "red" and COLOR2 == "blue") or (COLOR1 == "blue" and COLOR2 == "red"):
    print("Violet")
elif (COLOR1 == "yellow" and COLOR2 == "blue") or (COLOR1 == "blue" and COLOR2 == "yellow"):
    print("Green")
else:
    print("Error")
