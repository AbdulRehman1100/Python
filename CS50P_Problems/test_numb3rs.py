from numb3rs import validate

def test_format():
    assert validate("102.255.15.12") == True
    assert validate("192..147.57.15") == False
    assert validate("xyz.234.24.246") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False

def test_ranges():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255.198.76.256") == False
    assert validate("-1.0.0.0") == False