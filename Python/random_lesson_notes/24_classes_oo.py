class Student:
    def __init__(self, name, house, patronus):
        # same thing as name is blank
        if not name: #if name is blank
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): #this function prints the values of student
        #needs to be implemented otherwise Student returns value in memory
        return f"{self.name} from {self.house}"

    def charm(self):
        #by convention, inside a class, always use self in functions, 
        # even if you don't plan to use it
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Dog":
                return "🐶"
            case "Cat":
                return "😼"
            case _:
                return "🧙‍♂️"


def main():
    student = get_student()
    #print(f"{student.name} from {student.house}")
    print ("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()