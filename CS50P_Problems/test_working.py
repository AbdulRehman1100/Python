import pytest
import working

def test_format():
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        working.convert("12:50 AM, 13:00 PM")
    with pytest.raises(ValueError):
        working.convert("12:50 AM and 13:00 PM")
    with pytest.raises(ValueError):
        working.convert("12:50 AM-13:00 PM")

def test_range():
    with pytest.raises(ValueError):
        working.convert("0:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        working.convert("9:00 AM to 13:00 PM")

def test_no_mins():
    assert working.convert("12 AM to 11 PM") == "00:00 to 23:00"
    assert working.convert("7:30 AM to 1 PM") == "07:30 to 13:00"
    assert working.convert("7:00 AM to 1:30 PM") == "07:00 to 13:30"