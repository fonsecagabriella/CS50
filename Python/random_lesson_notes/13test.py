from calculator import square

def main():
    test_square()

def test_square():
    """option 01
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
        """
    # you can use assert, if condition met nothing happens
    # if cant assert returns error
    assert square(2) ==4
    assert square(3)== 9

"""
    pytest is a 3rd party app you can use for testing

    in the command line run 
    pytest calculator.py

    You can alo create a folder with tests 
"""

if __name__ == "__main__":
    main()  
