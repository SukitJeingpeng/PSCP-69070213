"""main water"""

TEMPERATURE = int(input())
TEMPERATURENAME = input().lower()

if TEMPERATURENAME == "f":
    TEMPERATURE -= 32

if TEMPERATURE <= 0:
    print("solid")
elif TEMPERATURE >= 100:
    print("gas")
else:
    print("liquid")
