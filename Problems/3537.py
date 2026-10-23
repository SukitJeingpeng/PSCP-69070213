"""IMPOSTOR"""

ALIVE_PLAYERS = {}
DEAD_PLAYERS = {}

while True:
    TEXT_LINE = input().strip()

    if TEXT_LINE == "Start":
        break

    CLEAN_LINE = TEXT_LINE.replace("{", "").replace("}", "").replace('"', "").replace("'", "")
    PARTS = CLEAN_LINE.split(":")

    PLAYER_NAME = PARTS[0].strip()
    PLAYER_ROLE = PARTS[1].strip()

    ALIVE_PLAYERS[PLAYER_NAME] = PLAYER_ROLE

while True:
    VOTED_NAME = input().strip()

    if VOTED_NAME == "End":
        break

    if VOTED_NAME in ALIVE_PLAYERS:
        ROLE_OF_DEAD = ALIVE_PLAYERS.pop(VOTED_NAME)
        DEAD_PLAYERS[VOTED_NAME] = ROLE_OF_DEAD

ALL_ROLES = list(ALIVE_PLAYERS.values())
REMAINING_IMPOSTORS = ALL_ROLES.count("Impostor")

print(f"{REMAINING_IMPOSTORS} Impostor Remains")

print("***Alive***")
SORTED_ALIVE = sorted(ALIVE_PLAYERS.items())
for PLAYER_NAME, PLAYER_ROLE in SORTED_ALIVE:
    RESULT_LINE = f"{PLAYER_NAME} : {PLAYER_ROLE}"
    print(RESULT_LINE)

print("***Dead***")
SORTED_DEAD = sorted(DEAD_PLAYERS.items())
for PLAYER_NAME, PLAYER_ROLE in SORTED_DEAD:
    RESULT_LINE = f"{PLAYER_NAME} : {PLAYER_ROLE}"
    print(RESULT_LINE)
