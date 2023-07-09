import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # (?i) allows case-sensitive matching
    matches = re.search(r"(?i)^<iframe (?:.+)(?:src=\"https?//)?(?:www\.)?(?:youtube\.com|youtu\.be)/embed/([a-zA-Z0-9_-]+)", s)

    if matches:
        return "https://youtu.be/" + str(matches.group(1))
    else:
        return "None"





if __name__ == "__main__":
    main()