"""PAD THAI"""

REQUIRED_IN = {
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts",
}

REQUIRED_FLAVORS = {
    "Sweet",
    "Sour",
    "Salty",
}

INGREDIENTS = set()
while True:
    ITEM = input().strip()
    if ITEM == "Cook":
        break
    INGREDIENTS.add(ITEM)

FLAVORS = set()
while True:
    ITEM = input().strip()
    if ITEM == "End":
        break
    FLAVORS.add(ITEM)

WRONG_INGREDIENT = not INGREDIENTS.issubset(REQUIRED_IN)
INCOMPLETE = INGREDIENTS != REQUIRED_IN
DELICIOUS = FLAVORS == REQUIRED_FLAVORS

if WRONG_INGREDIENT:
    print("This is not Pad Thai!!!")
elif INCOMPLETE:
    print("This is bad!")
elif DELICIOUS:
    print("Delicious!")
else:
    print("Not Bad...")
