def main():
    great_question()

def great_question():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if (is_42(answer)):
        print("Yes")
    else:
        print("No")

def is_42(answer):
    # clean answer for strip and puts all in lower-case for matching
    answer = answer.strip().lower()

    # performs match
    match answer:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


if __name__ == "__main__":
    main()

