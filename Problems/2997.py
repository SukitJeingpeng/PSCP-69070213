'''MAIN'''
RA = float(input())
RB = float(input())
PLAYER = input()

EA = 1/(1+(10**((RA-RB)/400)))
AE = 1/(1+(10**((RB-RA)/400)))

if PLAYER == "B":
    print(f"{EA:.2f}")
elif PLAYER == "A":
    print(f"{AE:.2f}")
