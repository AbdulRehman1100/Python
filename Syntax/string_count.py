
str1 = "    The quick brown fox"

for c in " abcdefghijklmnopqrstwxyz":
    print(c, str1.count(c))
    print(c.upper(), str1.count(c.upper()))
print("qu", str1.count("qu"))