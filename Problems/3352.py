"""LAST DIGIT"""

TEXT = input().replace("[", "").replace("]", "")

for num in TEXT.split(","):
    print(num.strip()[-1])
