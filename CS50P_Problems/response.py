from validator_collection import checkers, errors

email = input("What's your email address? ")
if (checkers.is_email(email)):
    print("Valid")
else:
    print("Invalid")