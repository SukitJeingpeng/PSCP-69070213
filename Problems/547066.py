'''MAIN'''

Month = int(input())
Day = int(input())

if Month in (1,2,3):
    if Month == 3 and Day >= 21:
        print("spring")
    else:
        print("winter")
elif Month in (4,5,6):
    if Month == 6 and Day >= 21:
        print("summer")
    else:
        print("spring")
elif Month in (7,8,9):
    if Month == 9 and Day >= 21:
        print("fall")
    else:
        print("summer")
elif Month in (10,11,12):
    if Month == 12 and Day >= 21:
        print("winter")
    else:
        print("fall")
