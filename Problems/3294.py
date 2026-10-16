"""Teaching schedule"""

TIMES = int(input())
DURATION = int(input())
TOTAL = TIMES * DURATION

HOURS = TOTAL // 60
MINUTES = TOTAL - (HOURS * 60)

if HOURS and MINUTES:
    print(f"{HOURS} hours {MINUTES} minute")
elif HOURS and not MINUTES:
    print(f"{HOURS} hours")
elif not HOURS and MINUTES:
    print(f"{MINUTES} minute")
else:
    print("No teaching")
