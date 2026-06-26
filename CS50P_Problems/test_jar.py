from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("seven")

def test_str():
    jar = Jar()
    assert jar.__str__() == ""
    jar.deposit(1)
    assert jar.__str__ ()== "🍪"
    jar.deposit(11)
    assert jar.__str__() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar.deposit(3)
    assert jar.size == 3    

def test_widthdraw():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(6)
    jar.deposit(2)
    jar.withdraw(3)
    assert jar.size == 2
