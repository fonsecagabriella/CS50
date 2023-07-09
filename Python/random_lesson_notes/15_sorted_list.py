names = []

with open("/Users/gabi/Desktop/phyton/names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"helo, {name}") 