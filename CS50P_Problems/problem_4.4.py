import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

number = random.choice(range(1, level+1))

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        if guess == number:
            print("Just right!")
            break
        elif guess < number:
            print("Too small!")
        else:
            print("Too large!")
    except ValueError:
        continue