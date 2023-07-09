from jar import Jar
import pytest

def test_init():
    # ensures when object is created without valued, size = 0 and capacity = 12
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0


    # ensures that object gets capacity passed by used
    jar = Jar(10)

    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    #try to deposit more than capacity
    one_more = jar.capacity + 1

    with pytest.raises(ValueError):
        jar.deposit(one_more)


def test_withdraw_more():
    jar = Jar()

    #try to withdraw more than capacity
    one_more = jar.capacity + 1

    with pytest.raises(ValueError):
        jar.withdraw(one_more)

def test_withdraw_count():
    # create a jar with capacity 10
    jar = Jar(10)

    # deposits 10 cookies
    jar.deposit(10)

    # take 2 cookies, remains 8
    jar.withdraw(2)

    # take another 3 cookies, because hungry, remain 5
    jar.withdraw(3)

    # return amount of cookies, should be five
    assert str(jar) == "🍪" * 5

