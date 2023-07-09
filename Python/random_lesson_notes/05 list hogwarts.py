#using dictionary
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor", 
            "Rony": "Gryffindor",
             "Draco": "Slytherin", }

# look for hermione key
print(students["Hermione"])

for student in students:
    #the first one prints the key, or the name of student. the second uses the value of student to go into the dictionary
    print(student, students[student], sep=", ")

#printing the content of a list
""""
students = ["Hermione", "Harry", "Rony"]

for student in students:
    print(student)

"""


