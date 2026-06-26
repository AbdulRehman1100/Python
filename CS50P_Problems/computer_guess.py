
# In this program user think of a number and provide an lower and upper range
# computer guess the number and take feedback from the user whether the number is higher, lower, or correct

def take_user_response():
    user_reponse = input("Is computer guess higher,lower or correct (enter h/l/c): ").lower()
    while user_reponse not in ["l", "c", "h"]:
       user_reponse = input("Enter h for higher, l for lower and c for correct: ").lower()
    return user_reponse

print("\n\n******Number Guessing Game******")
print("But the suprise is, this time computer will guess the number.")
print("Player will tell the computer whether its guess is correct." )
print("If guess is not correct then player will tell whether the guess is lower or higher.")
print("But first of all enter lower and upper boundary of the range from which computer have to guess the number from.")

lower_boundary = input("\nEnter range lower boundary: ")
while not lower_boundary.isdecimal():
      lower_boundary = (input("Enter an integer lower boundary: "))
lower_boundary = int(lower_boundary)

upper_boundary = input("\nEnter range upper boundary: ")
while not upper_boundary.isdecimal():
      upper_boundary = input("Enter integer range upper boundary: ")
upper_boundary = int(upper_boundary)

middle = (lower_boundary + upper_boundary)//2
print(f"\nComputer guessed: {middle}")

user_reponse = take_user_response()

while user_reponse != "c":
    if user_reponse == "h":
            lower_boundary = middle + 1
    elif user_reponse == "l":
           upper_boundary = middle - 1

    middle = (lower_boundary + upper_boundary)//2
    print(f"\nComputer guessed: {middle}")

    user_reponse = take_user_response()

print("\nYeah, I can read your mind")