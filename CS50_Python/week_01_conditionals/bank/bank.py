def main():
    user_greeting()

def user_greeting():
    greeting = input("what is your greeting? ")
    greeting = format_string(greeting)

    check_greeting(greeting)

def format_string(s):
    return s.strip().lower()

def check_greeting(g):
    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()