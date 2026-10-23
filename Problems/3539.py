"""IPHONE 13 AGAIN"""

PRICES = {
    "iPhone 13 mini": {
        "128 GB": 25900,
        "128GB": 25900,
        "256 GB": 29900,
        "256GB": 29900,
        "512 GB": 37900,
        "512GB": 37900,
    },
    "iPhone 13": {
        "128 GB": 29900,
        "128GB": 29900,
        "256 GB": 33900,
        "256GB": 33900,
        "512 GB": 41900,
        "512GB": 41900,
    },
    "iPhone 13 Pro": {
        "128 GB": 38900,
        "128GB": 38900,
        "256 GB": 42900,
        "256GB": 42900,
        "512 GB": 50900,
        "512GB": 50900,
        "1 TB": 58900,
        "1TB": 58900,
    },
    "iPhone 13 Pro Max": {
        "128 GB": 42900,
        "128GB": 42900,
        "256 GB": 46900,
        "256GB": 46900,
        "512 GB": 54900,
        "512GB": 54900,
        "1 TB": 62900,
        "1TB": 62900,
    },
}

MODEL = input().strip()
CAPACITY = input().strip()

if MODEL in PRICES and CAPACITY in PRICES[MODEL]:
    print(PRICES[MODEL][CAPACITY])
else:
    print("Not Available")
