"""WAREHOUSE MANAGEMENT SYSTEM"""

STOCK = {}

while True:
    LINE = input().strip()
    if LINE == "END":
        break

    PARTS = LINE.split()
    COMMAND = PARTS[0]

    if COMMAND == "ADD":
        ITEM = PARTS[1]
        AMOUNT = int(PARTS[2])
        if ITEM in STOCK:
            STOCK[ITEM] += AMOUNT
        else:
            STOCK[ITEM] = AMOUNT

    elif COMMAND == "REMOVE":
        ITEM = PARTS[1]
        AMOUNT = int(PARTS[2])
        if ITEM in STOCK and STOCK[ITEM] >= AMOUNT:
            STOCK[ITEM] -= AMOUNT
        else:
            STOCK[ITEM] = 0
            print(f"Not enough stock for {ITEM}")

    elif COMMAND == "CHECK":
        LOW_STOCK_ITEMS = []
        for item, amount in STOCK.items():
            if amount < 5:
                LOW_STOCK_ITEMS.append(item)

        if LOW_STOCK_ITEMS:
            for item in sorted(LOW_STOCK_ITEMS):
                print(item)
        else:
            print("All stocks are sufficient")

    elif COMMAND == "REPORT":
        for item, amount in sorted(STOCK.items()):
            print(f"{item}: {amount}")
