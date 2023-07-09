import numb3rs
import sys

def main():
    test_validate()
    #test_is_ip_format()
    #test_valid_digits()
    #sys.exit(0)



def test_validate():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("512.521.255.255") == False
    assert numb3rs.validate("75.456.76.65") == False # test to pass catches numb3rs.py only checking if first byte of IPv4 address is in range
    assert numb3rs.validate("1.2.3.1000") == False
    assert numb3rs.validate("0.2.3.1000") == False
    assert numb3rs.validate("cat") == False


"""

def test_is_ip_format():
    # Correct format
    assert numb3rs.is_ip_format("123.233.123.123") == True
    # Returns true here because checks format, not digits. Tested in valid_digits or main returns False
    assert numb3rs.is_ip_format("123.233.123.333") == True
     # Incorrect formats
    assert numb3rs.is_ip_format("cat") == False
    assert numb3rs.is_ip_format(".233.123.123") == False
    assert numb3rs.is_ip_format("123.233.123.") == False
    assert numb3rs.is_ip_format("123..123.1") == False
    assert numb3rs.is_ip_format("cat.cat.123.1") == False

def test_valid_digits():
    # One higher than 256
    assert numb3rs.valid_digits("123.233.123.333") == False
    assert numb3rs.valid_digits("123.233.123.256") == False
    # All between 0 and 255
    assert numb3rs.valid_digits("123.233.123.255") == True
    assert numb3rs.valid_digits("123.233.123.0") == True

"""
if __name__ == "__main__":
    main()