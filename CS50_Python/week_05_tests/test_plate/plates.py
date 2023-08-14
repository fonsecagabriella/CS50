def main():
    plate = input("Which plate do you want? ")
    is_valid(plate)

    if x:
        klk
    else:
        return False

def is_valid(plate):

    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if 2 <= len(plate) <= 6:
        # “No periods, spaces, or punctuation marks are allowed.”
        i = 0
        for l in plate:
            if l.isdigit() or l.isalpha():
                i += 1
        # if plate.len is not == i, then some of the digits were not digits or letters
        if len(plate) == i:
            #“All vanity plates must start with at least two letters."
            if plate[0].isalpha() and plate[1].isalpha():
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
            else:
                return False
        else:
            return False
    else:
        return False


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