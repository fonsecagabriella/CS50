import random

'''
You use class methods when you have only one of something
Like in HP you only have one Sorting Hat
'''

class Hat:
    # I don't use self because houses will be used in any function, 
    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]

    #use cls not self
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# don't need to instantiate the object, because there is only one
Hat.sort("Harry")