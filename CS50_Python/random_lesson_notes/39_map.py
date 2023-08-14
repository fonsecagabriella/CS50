def main():
    yell("This", "is", "cs50")

def yell(*words):
    #map allows you to apply a function to a list
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()
