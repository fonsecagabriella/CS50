def main():
    s = input("Give me some text to play with: ")
    convert(s)

def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return print(s)

if __name__ == "__main__":
    main()