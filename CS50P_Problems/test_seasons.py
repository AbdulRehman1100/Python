from seasons import calculate_minutes, minutes_to_words
from datetime import date, timedelta

def test_minutes_to_words():
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_words(60) == "Sixty minutes"
    assert minutes_to_words(0) == "Zero minutes"

def test_calculate_minutes():
    assert calculate_minutes(date.today()) == 0
    yesterday = date.today() - timedelta(days=1)
    assert calculate_minutes(yesterday) == 24 * 60