import re

# email = input("What's your email? ").strip()

# if re.search(r".+@.+\.edu", email):
#     print("Valid")
# else:
#     print("Invalid")

txt = "This is Spain"
x = re.search("^This.*Spain$", txt)
if x:
    print("Yes we have match")
else:
    print("No match")

