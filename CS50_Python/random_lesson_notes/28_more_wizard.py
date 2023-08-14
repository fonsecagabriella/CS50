class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


# this is a way to say a Student is a Wizard, and inherits their attributes
class Student(Wizard):
    def __init__(self, name, house):
        # this is a reference to the super class, this case Wizard
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)        
        self. subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")