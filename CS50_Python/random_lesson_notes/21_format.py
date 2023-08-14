import re

name = input("What's your name? ").strip()


#the below will take the cases users write their name as LAST, FIRST
# the ( )  groups itens
# so if the below returns POSITIVE, the if will run
matches = re.search(r"^(.+), (.+)+$", name)

if matches:
    last, first = matches.groups()
    # alternative use first = matches.group(2)  and last = matches.group(1)


# the Walrus operator can assign the value from left to right AND
# check if true at the same time := 
# EXAMPLE
# matches := re.search(r"^(.+), (.+)+$", name)
#   last, first = matches.groups()    

print(f"hello, {name}")