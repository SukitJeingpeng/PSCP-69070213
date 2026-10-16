"""ตั๋วหนังสุดป่วน"""

TICKETS = int(input())
while TICKETS > 0:
    AGE,TOTAL = input().split()
    AGE = int(AGE)
    TOTAL = int(TOTAL)
    COST = 150 * TOTAL
    if AGE < 15:
        print(-1)
    elif TOTAL > TICKETS:
        print(-2)
    else:
        if AGE <= 22:
            PAY = COST * 0.8
        elif AGE >= 60:
            PAY = COST *0.5
        else:
            PAY = COST
        TICKETS -= TOTAL
        print(int(PAY), end=" ")
        print(TICKETS)
