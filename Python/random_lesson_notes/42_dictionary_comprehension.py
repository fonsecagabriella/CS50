print("SOLUTION 01 \n\n")
students = [ "Hermione", "Harry", "Ron" ]
gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)

#########
print("\n\n ########### \n\n")
print("SOLUTION 02 \n\n")

# this is an example of list comprehension
# create the list on the go
g = [{"name": student, "house": "Gryffindor"} for student in students]

print(g)

#########
print("\n\n ########### \n\n")
print("SOLUTION 03 -  \n\n")

# this is an example of DICTIONARY comprehension
# create the list on the go
gd = {student: "Gryffindor"  for student in students}

print(gd)
