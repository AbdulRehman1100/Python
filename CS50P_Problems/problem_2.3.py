txt = input("Input: ").strip()
# txt_without_vowels = []
# for c in txt:
#     if c not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
#         txt_without_vowels.append(c)
# print("".join(txt_without_vowels))

# And a more Pythonic approach using list comprehension:
print("".join(c for c in txt if c.lower() not in "aeiou"))