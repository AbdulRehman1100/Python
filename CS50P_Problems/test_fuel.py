from fuel import convert, gauge 
import pytest

def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/2")

def test_noninteger_fraction():
    with pytest.raises(ValueError):
        convert("a/b")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_percentages():
    assert convert("4/4") == 100
    assert convert("1/100") == 1
    assert convert("2/3") == 67
    assert convert("2/4") == 50

def test_F():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) != "F"

def test_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(2) != "E"

def test_other_level():
    assert gauge(45) == "45%"
    assert gauge(90) == "90%"
