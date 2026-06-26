import random

words = ["apple", "mango", "python", "chair", "market"]
secret_word = random.choice(words)
lives = 6
guessed_letters = []
secret_word_placeholder = ["-" for x in range(len(secret_word))]

while(lives > 0 and "".join(secret_word_placeholder) != secret_word):
    guess = input("\nEnter the letter: ").lower()
    while guess in guessed_letters:
        print(f"{guess} already guessed")
        guess = input("\nEnter the letter: ").lower()
    else:
        guessed_letters.append(guess)

    secret_word_placeholder_cpy = secret_word_placeholder[:] 
    for index, letter in enumerate(secret_word):
        if letter == guess:
            secret_word_placeholder[index] = guess

    if secret_word_placeholder_cpy != secret_word_placeholder:
        print(secret_word_placeholder)
    else:
        lives -= 1
        print("Wrong guess")
        print(f"Remaining lives {lives}")

if("".join(secret_word_placeholder)  == secret_word):
    print("\nCongratulation, You Won!")
else:
    print("\nBetter luck!, next time")
