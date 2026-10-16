"""CHRISTMAST"""

COLOR, TIMES = input().split()
COLOR = COLOR.upper()
TIMES = int(TIMES)
COLORLOOP = []
START = 0

if COLOR == "R":
    COLORLOOP = ["Red","Green","Blue"]
elif COLOR == "G":
    COLORLOOP = ["Green","Blue","Red"]
elif COLOR == "B":
    COLORLOOP = ["Blue","Red","Green"]

for i in range(TIMES):
    print(COLORLOOP[START + (i%3)], end=" ")
