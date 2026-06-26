from bank import value

def test_start_with_hello():
    assert value("hello") == 0

def test_start_with_Hello():
    assert value("Hello, how are you?") == 0

def test_start_with_HELLO():
    assert value("HELLO") == 0
    
def test_start_with_h():
    assert value("h") == 20

def test_start_with_What():
    assert value("What's up?") == 100

def test_start_with_How():
    assert value("How are you?") == 20