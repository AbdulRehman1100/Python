x = range(10)
print(x, type(x))
guess = int(input("Please enter a number: "))
if(guess in x):
    print("The membership operator returns:", guess in x)
    print("The entered number is in range")
else:
    print("The entered number is not in range")
