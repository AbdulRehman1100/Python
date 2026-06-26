from plates import is_valid

def test_too_short():
    assert is_valid("A") == False


def test_minimum_length():
    assert is_valid("AA") == True

def test_maximum_length():
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False

def test_start_letters():
    assert is_valid("ABCDEF") == True
    assert is_valid("XYZ") == True

def test_0_not_first_digit():
    assert is_valid("AA0123") == False

def test_no_punctuation():
    assert is_valid("AA...") == False
    assert is_valid("AA 12") == False

def test_letters_digit():
    assert is_valid("12AAAA") == False
    assert is_valid("AB1234") == True
    assert is_valid("AA12AA") == False
