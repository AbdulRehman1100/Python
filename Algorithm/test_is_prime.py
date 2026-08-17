from is_pime import is_prime
import pytest

def test_is_prime_none_integer():
    with pytest.raises(TypeError):
        is_prime(2.0)
    with pytest.raises(TypeError):
        is_prime(6.35)
    with pytest.raises(TypeError):
        is_prime("abc")

def test_is_prime_non_positive_numbers():
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(-2) == False
    assert is_prime(-9) == False

def test_is_prime_for_number_one():
    assert is_prime(1) == False

def test_is_prime_for_number_two():
    assert is_prime(2) == True


def test_is_prime_for_successes():
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True
    assert is_prime(23) == True
    assert is_prime(29) == True
    assert is_prime(31) == True

def test_is_prime_for_failures():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(18) == False
