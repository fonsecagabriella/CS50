# code filename.py 
# creates file when typed in terminal

x = input("wat is x? ")
y = input("wat is y? ")

z= float(x) + float(y)

#print(z)

# fancy way of writing
print(f"{z:,}")

# fancy way of writing number with 2 digits
print(f"{z:.2f}")

"""
TYPES OF NUMBERS
int
float

NUMBER FUNCTIONS
round(number, [, ndigits]) -- example round(x,y, 2) : rounds to 2 digits

"""