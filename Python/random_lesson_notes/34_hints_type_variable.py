# In Python you don't have a way to set a specific type of variable
# but you can product hints

# on command line
#pip install mypy

# Check if variables are using the right pipe


# you need to run in the command line
# mypy meow.py
# to see potentital errors with types

# the n: int is a hint
# The _> None is a hint that the default value of a function is None
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

def meouw_right(n: int) -> str:
    return "meow \n" * n

# the input function gets a string, not an intenger
# so you need to conver the interger
# or you have to use the hint

number: int = int(input("Number: ")) 
meow(number)

print("|------------------|")

# the end="" removes the last \n assigned in the code
print ((meouw_right(number)), end="")