def main():
    #print_row(4)
    #print_column(3)
    #print("ei")
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        # for each brick in row
        for j in range (size):
            print ("#", end="")

        #for each brick in row
        print()



def print_column(heigh):
    for _ in range(3):
        print ("#")

def print_row(width):
    print ("?" * width)

#não esquece da porra do () pra chamar função
main()
