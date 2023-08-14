students = []

with open("/Users/gabi/Desktop/phyton/names_house.csv") as file:
    for line in file:
        """Option 01
        row = line.rstrip().split(",")
        print(f"{row[0]} is in{row[1]}")
        """
        name, house = line.rstrip().split(",")

        #create a dictionary
        student = {"name": name, "house": house}

        # alternative to above
        #student = {}
        #student["name"] = name
        #student["house"] = house

        students.append(student)

def get_name(student):
    #gets the name of the student in the dictionary
    return student["name"]

# in python you can also use functions for returning 
for student in sorted(students, key=get_name):
        print(f"{student['name']} is in{student['house']}")


# Alternatively, can use lambda funciton, as function doesn't get used in other parts of the code
# lambda is an anonymous functions
# for student in sorted(students, key=lambda student: student["name"]):
