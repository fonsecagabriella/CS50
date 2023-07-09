import plates

def main():
    test_valid()

def test_valid():

    # tests all rules in combination
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA22A") == False
    assert plates.is_valid("AAA023") == False
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("CS50P") == False
    assert plates.is_valid("PI3.14") == False
    assert plates.is_valid("G") == False
    assert plates.is_valid("OUTATIME") == False
    assert plates.is_valid("IMGABI") == True
    assert plates.is_valid("IMGAB1") == True
    assert plates.is_valid("IMG481") == True

    assert plates.is_valid("123ABC") == False
    assert plates.is_valid("**AB12") == False





def test_start_with_two_letters():
    # “All vanity plates must start with at least two letters.”
    assert plates.is_valid("hh") == True
    assert plates.is_valid("hG") == True
    assert plates.is_valid("HI") == True
    assert plates.is_valid("G0") == False
    assert plates.is_valid("h0") == False
    assert plates.is_valid("_h") == False

def test_check_len():
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    assert plates.is_valid("ABC123") == True
    assert plates.is_valid("123ABC") == False
    assert plates.is_valid("AB") == True
    assert plates.is_valid("A") == False
    assert plates.is_valid("**AB12") == False

def test_check_numbers_letters():
    # “No periods, spaces, or punctuation marks are allowed.”
    assert plates.is_valid("ABC123") == True
    assert plates.is_valid("AB CD") == False
    assert plates.is_valid("12_N*D") == False
    assert plates.is_valid("Buy.ME") == False
    assert plates.is_valid("**AB12") == False  # but tested in test_check_len() returns True

def test_check_ends_with_number():
    #“Numbers cannot be used in the middle of a plate;
    # they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”

    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA22A") == False
    assert plates.is_valid("AAA022") == False
    assert plates.is_valid("A22222") == False 


if __name__ == "__main__":
    main()