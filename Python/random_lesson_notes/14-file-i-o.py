name = input("Hoe heet je?")

#w for write
# the code works by every time it creates a new file, that overwrites the one from before
#file = open("/Users/gabi/Desktop/phyton/names.txt", "w")




""" One option 
# a for append
file = open("/Users/gabi/Desktop/phyton/names.txt", "a")

file.write(f"{name}\n") 
file.close()

"""

# this way you have no issues of forgeting to close your file
with open("/Users/gabi/Desktop/phyton/names.txt", "a") as file:
    file.write(f"{name}\n")


# to READ
with open("/Users/gabi/Desktop/phyton/names.txt", "r") as file:
    lines = file.readlines()

# Second option, more compact , if sorting not needed   
#    for line in file:
#        print(f"Hello, {line.rstrip()}\n")


for line in lines:
    print(f"Hello, {line.rstrip()}\n")