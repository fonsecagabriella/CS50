students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

#### FILTERS
print("\n###########\nEXAMPLE 2 \n\n")

def is_gry(s):
    return s["house"] == "Gryffindor"

# this is similar to map
# passes a function that return true or false
# and the list to be verified

gryffindors_filter = filter(is_gry, students)

for g in gryffindors_filter:
    print(g["name"])