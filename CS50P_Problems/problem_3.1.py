while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        result = round(x / y * 100)
        break  # only exit loop if everything is valid
    except (ValueError, ZeroDivisionError):
        pass  # loop again

if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")