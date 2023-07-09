# Constants do not properly exist in Python
# we can implement the notion of it
# with the convetion below

''' OPTION 01
MEOWS = 3

for _ in range(MEOWS):
    print("meow")


'''

class Cat:
    MEOW = 3

    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow")


cat = Cat()

cat.meow()