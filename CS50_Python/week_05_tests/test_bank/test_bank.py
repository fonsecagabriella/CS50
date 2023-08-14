import bank

def main():
    test_value()

def test_value():
    test_case_0()
    test_case_20()
    test_case_100()

def test_case_0():
    # if string starts with hello, returns 0, ignores case
    assert bank.value("hello there") == 0
    assert bank.value("HELLO there") == 0
    assert bank.value("hElLo there") == 0

def test_case_20():
    # if string starts with h but not hello, returns 20
    assert bank.value("hi mark") == 20
    assert bank.value("horizontal lines") == 20

def test_case_100():
    # if string starts with anything else, returns 100
    assert bank.value("--hello") == 100
    assert bank.value("boing") == 100
    assert bank.value("cs50") == 100
    assert bank.value("123hello") == 100

if __name__ == "__main__":
    main()