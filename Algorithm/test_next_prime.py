from next_prime import next_prime
import pytest

def test_next_prime_none_integer():
    with pytest.raises(TypeError):
        next_prime(2.0)
    with pytest.raises(TypeError):
        next_prime(6.35)
    with pytest.raises(TypeError):
        next_prime("abc")

def test_next_prime_none_positive_integers():
    assert next_prime(0) == 2
    assert next_prime(-1) == 2
    assert next_prime(-2) == 2
    assert next_prime(-9) == 2

def test_next_prime_for_postive_integers():
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(5) == 7

    assert next_prime(20) == 23
    assert next_prime(44) == 47