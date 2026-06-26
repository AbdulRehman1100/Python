import random


def main():
    level = get_level()
    score = 0
    no_of_questions = 10
    while no_of_questions > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        attempt = 3
        while attempt > 0:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                attempt -= 1
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")   
            except ValueError:
                attempt -= 1
                continue
        else:
            print(f"{x} + {y} = {answer}")

        no_of_questions -= 1
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    if level == 1:
        return random.choice(range(0, 10))
    elif level == 2:
        return random.choice(range(10, 100))
    elif level == 3:
        return random.choice(range(100, 1000))


if __name__ == "__main__":
    main()