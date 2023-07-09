import sys
import re
from datetime import datetime
from datetime import date
import inflect # generate plurals, singular nouns, ordinals, indefinite articles, convert numbers to words


def main():
    bday = is_date(input("Date of Birth: "))
    n = number_in_words((minutes_alive(bday)))
    print(n + " minutes")

def is_date(s):

    try:
        if not re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s):
            print("Invalid format")
            sys.exit(1)
        else:
            #return datetime.strptime(s, "%Y-%m-%d")
            return date.fromisoformat(s)
    except ValueError:
        print("Invalid date")
        sys.exit(1)


def minutes_alive(birth):
    today = date.today()
    delta = today - birth
    return delta.days * 60 * 24


def number_in_words(n):
    # https://pypi.org/project/inflect/
    p = inflect.engine()
    return p.number_to_words(n, andword="").capitalize()

if __name__ == "__main__":
    main()