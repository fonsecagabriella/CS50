import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    # regex to look for um
    pattern = r"\bum\b"
    match = re.findall(pattern, s, re.IGNORECASE)

    return len(match)


if __name__ == "__main__":
    main()