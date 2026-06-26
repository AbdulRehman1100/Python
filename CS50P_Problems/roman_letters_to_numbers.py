def from_roman_numeral(roman_numeral):
    roman_numerls = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for index, letter in enumerate(roman_numeral):
        if index == len(roman_numeral) - 1:
            total += roman_numerls[letter]
        elif roman_numerls[letter] < roman_numerls[roman_numeral[index+1]]:
            total -= roman_numerls[letter]
        else:
            total += roman_numerls[letter]
    return total


print(from_roman_numeral("IV"))    # → should be 5
print(from_roman_numeral("XX"))   # → should be 20
print(from_roman_numeral("DCCC")) # → should be 800
print(from_roman_numeral("MMMM"))  #→ should be 4000
