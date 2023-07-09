def main():
    number = get_number()
    meow(number)
    print("hi")

def get_number():
    while True:
        n = int(input("What is n?"))
        if n >0:
            break        
    return n

def meow(n):
    for _ in range (n):
        print ("meow")



main()