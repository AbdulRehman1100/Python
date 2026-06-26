from twttr import shorten

def test_lowercase_vowels():
    assert shorten("movie") == "mv"

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"

def test_mixcase_vowels():
    assert shorten("VowEls") == "Vwls"

def test_no_vowels():
    assert shorten("Sky") == "Sky"

def test_special_characters():
    assert shorten(".@12") == ".@12"
