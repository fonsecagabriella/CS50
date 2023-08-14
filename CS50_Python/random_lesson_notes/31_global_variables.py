# balance here is a global variable
# for convention is goes on the top of the file
# the global needs to go in the functions that use it as an indicator
# the variable is global

# it is better to use the solution in file 32 than this global variable 

balance = 0

def main():
    print("Balance:", balance)

    deposit(100)
    withdraw(50)

    print("New balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()