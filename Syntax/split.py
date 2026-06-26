
txt = "Thank you for your music\nWelcome to the jungle."
# strlines = txt.splitlines();
# print(strlines)

# strlines = txt.splitlines(True)
# print(strlines)

# n Python, split() already treats all
# whitespace (' ', '\n', '\t', etc.) as separators when you don't pass a separator.
str_words = txt.split() 
print(str_words)

# str_words = txt.split("o")
# print(str_words)

str_words = txt.split(maxsplit = 4)
print(str_words)


