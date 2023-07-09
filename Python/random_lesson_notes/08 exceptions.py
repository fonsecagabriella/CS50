def main():
    x = get_int()
    print(f"x is {x:.2f}")

def get_int():
    # this programm will loop forever until users passess an integer
    while True:
        try:
            x= int (input("What's x? "))
        except ValueError:
            print("x is not intenger")
            # you can use pass here if you don't want to do anything with error
            # pass
        else: #if the try succeeds, than executes command below
            break;

    # this is not going to trigger error because program only comes here when
    #  the x is defined on the step before
    #print(f"x is {x:.2f}")

    # you dont need to use both return and break, return is stronger than break and 
    # kind of brings break when you call it
    return x



main()