def main():
    yell("This", "is", "cs50")

def yell(*words):
    #another way to do example 39
    # this is called list comprehension
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
