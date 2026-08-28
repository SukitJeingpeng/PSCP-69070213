"""EXPRESS DELIVERY"""

ROUTE = input()
WEIHGT = float(input())
ERROR = False
BASEFEE = 0
WEIGHTFEE = 0

if ROUTE == "BKK CNX":
    BASEFEE = 10
    WEIGHTFEE = 30
elif ROUTE == "CNX UBP":
    BASEFEE = 15
    WEIGHTFEE = 40
elif ROUTE == "UBP BKK":
    BASEFEE = 20
    WEIGHTFEE = 40
elif ROUTE == "BKK PKT":
    BASEFEE = 25
    WEIGHTFEE = 50
elif ROUTE == "PKT CNX":
    BASEFEE = 30
    WEIGHTFEE = 60
elif ROUTE == "UBP PKT":
    BASEFEE = 40
    WEIGHTFEE = 70
else:
    ERROR = True

if ERROR:
    print("Error")
else:
    total = BASEFEE + (WEIHGT * WEIGHTFEE)
    print(f"{total:.2f}")
