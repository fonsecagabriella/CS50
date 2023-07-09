import working
import pytest

def main():
    test_convert()

def test_convert():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert working.convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_error_convert():
    # invalid hour / minutes
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:60 PM")
        working.convert("13:00 AM to 5 PM")

def test_value_error_extract_hours_minutes():
    # wrong format input
    with pytest.raises(ValueError):
        working.convert("9 AM -  5 PM")
        working.convert("9:00 AM - 17:00 PM")

if __name__ == "__main__":
    main()