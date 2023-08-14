# PROPERTIES
# Attributes you have more control over
# you use @property
# the @ is called decorator: a function that modifies the behaviour of another function

# IMPORTANT: variables and functions cannot have the same name
# convention use _ in setter


# There is no public, private, protected in Pythong
# so if a variable starts with _ conventions says: DO  NOT TOUCH IT
# although in practice you could change their value

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self): #this function prints the values of student
        #needs to be implemented otherwise Student returns value in memory
        return f"{self.name} from {self.house}"


    # This prevents is more safe, prevents the user from setting the house
    # from invalid value
    # the values for getter and setter need to be the same as the variables

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name (self):
        return self._name

    @name.setter
    def name(self, name):
        # same thing as name is blank
        if not name: #if name is blank
            raise ValueError("Missing name")
        self._name = name


def main():
    student = get_student()
    #print(f"{student.name} from {student.house}")
    print (student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()