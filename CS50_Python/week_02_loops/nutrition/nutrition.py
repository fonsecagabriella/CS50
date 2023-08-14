fruits = {
    "pear": 100,
    "apple": 130,
    "avocado": 50,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydrew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "sweet cherries": 100
}


fruit = input("Which fruit are you eating today? ").lower()

while True:
    try:
        print(f"Calories: {fruits[fruit]}")
        break
    except KeyError:
        break

