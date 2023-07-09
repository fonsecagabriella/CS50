def main():
    x= int(input("Whats is x?"))
    print("x squared is", square(x))

    y = int(input("What is y?"))

    compare(x,y)

    compare_option2 (x,y)

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def compare(x,y):
    if x > y:
        print("x is bigger than y")
    # the elfi tells only to look below if condition above was not met
    elif y > x:
        print("y is bigger than x")
    elif x==y:
        print("it is the same number bro")
    # this is the last option
    else:
        print("impossibru!")

def compare_option2(x,y):
    if x < y or x >y :
        print("x is not equal to y")
    else:
        print("hey, it is the same number")

def score_student(grade):
    #only in python you can do that
    if 80 <= grade <= 100:
        print("Grade A")
    elif 60 <= grade<80: 
        print("Grade B")
    else:
        print("Retake time!")

def is_even(n):
    return True if n % 2 == 0 else False

def square(n):
    return n * n

def hogwarts_house(name):
    match name:
        case "Harry" | "Hermione" | "Ronny"
            print ("Gryffindor")
        case "Draco":
            print ("Slytherin")
        case _:
            print("who?")
            


main()