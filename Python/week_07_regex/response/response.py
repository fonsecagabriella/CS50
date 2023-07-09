# pip install validador-collection
# https://validator-collection.readthedocs.io/en/latest/validators.html
from validator_collection import validators, errors #need to import errors, as raises specific errors


def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    try:
        validators.email(s, allow_empty = False) # allow_empty
        return "Valid"
    except Exception:
        return "Invalid"


if __name__ == "__main__":
    main()
