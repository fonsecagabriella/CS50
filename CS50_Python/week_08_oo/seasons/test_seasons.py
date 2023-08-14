import seasons
import pytest
import sys

def main():
    ...

def test_is_date_format():
    # wrong format, checks if exited in 1
    ...
    with pytest.raises(SystemExit) as exc_info:
        seasons.is_date("25 January 1991")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        seasons.is_date("25/January/1991")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        seasons.is_date("1991/01/25")
    assert exc_info.value.code == 1



def test_is_date_invalid_date():
    # dates that don't exist, but format
    with pytest.raises(SystemExit) as exc_info:
        seasons.is_date("1990-02-30")
    assert exc_info.value.code == 1

    with pytest.raises(SystemExit) as exc_info:
        seasons.is_date("1990-40-30")
    assert exc_info.value.code == 1


def test_number_in_words():
    assert seasons.number_in_words("30") == "Thirty"
    assert seasons.number_in_words("525600") == "Five hundred twenty-five thousand, six hundred"


if __name__ == "__main__":
    main()