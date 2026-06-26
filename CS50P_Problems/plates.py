def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0:2].isalpha():
            i = 2
            while i < len(s) and s[i].isalpha():
                i += 1
            if i != len(s):
                if s[i] == "0":
                    return False
                if s[i:].isnumeric():
                    return True
            else:
                return True
    return False


if __name__ == "__main__":
    main()