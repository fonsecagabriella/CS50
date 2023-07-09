def main():
    plate = input("Which plate do you want? ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    return check_len(plate) and check_numbers_letters(plate) and check_start_two_letters(plate) and check_ends_with_number(plate)

def check_len(plate):
   # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
   return 2 <= len(plate) <= 6

def check_numbers_letters(plate):
   # “No periods, spaces, or punctuation marks are allowed.”
   i = 0
   for l in plate:
       if l.isdigit() or l.isalpha():
           i += 1
   # if plate.len is not == i, then some of the digits were not digits or letters
   return len(plate) == i

def check_start_two_letters(plate):
   #“All vanity plates must start with at least two letters."
   return plate[0].isalpha() and plate[1].isalpha()

def check_ends_with_number(plate):
    #“Numbers cannot be used in the middle of a plate;
    # they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”

    pos_first_digit = None
    i = 0

    for l in plate:
        if l.isdigit():
           pos_first_digit = i
           break
        i += 1

    if pos_first_digit is not None:
        if plate[pos_first_digit] == "0":
            return False
        else:
            return plate[pos_first_digit:len(plate)].isdigit()
    else:
        return True


if __name__ == "__main__":
    main()