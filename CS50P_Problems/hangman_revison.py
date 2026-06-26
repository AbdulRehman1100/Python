# hangman game

import random

words = ["apple", "mango", "python", "chair", "market"]
secret_word = random.choice(words)
lives = 6
word_placeholder = ["-" for x in range(len(secret_word))]
guessed_letters = []

print("***********HangMan Game************")
print("You have to guess a random word before you run out of lives")
print("Rules:")
print(f"{lives} will given at start")
print("Guess a single character at time")
print("Number are not allowed")
print("Only wrong guess will cost a life")

while lives > 0 and "".join(word_placeholder) != secret_word:
    print(f"\nGuessed letters: {', '.join(guessed_letters)}")
    guess = input("Guess the word letter by letter: ")

    while len(guess) != 1 or not guess.isalpha():
        guess = input("Please enter a single character: ")

    while guess in guessed_letters:
        print(f"{guess} already guessed")
        print(f"\nGuessed letters: {', '.join(guessed_letters)}")
        guess = input("Enter the character you haven't guessed: ")

        while len(guess) != 1 or not guess.isalpha():
            guess = input("Please enter a single character: ")
    else:
        guessed_letters.append(guess)

    word_placeholder_cpy = word_placeholder[:]

    for index, letter in enumerate(secret_word):
        if letter == guess:
            word_placeholder[index] = guess

    if word_placeholder != word_placeholder_cpy:
        print(" ".join(word_placeholder))
    else:
        lives -= 1
        print("Wrong guess")
        print(f"Remaining Lives: {lives}")

if "".join(word_placeholder) == secret_word:
    print("\nCongratulation!, you won")
else:
    print("\nBetter luck!, next time")