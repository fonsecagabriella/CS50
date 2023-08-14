import fuel
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/3") == 33
    #assert fuel.convert("8/3") == pytest.raises(ValueError)
    #assert fuel.convert("8/0") == ZeroDivisionError

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("8/0")

def test_value_error():
    with pytest.raises(ValueError):
        fuel.convert("8/3")
        fuel.conver("cat")


def test_gauge():
    assert fuel.gauge(3) == "3%"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

if __name__ == "__main__":
    main()