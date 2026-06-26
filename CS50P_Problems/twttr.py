def main():
    pass


def shorten(word):
    return "".join(c for c in word if c.lower() not in "aeiou")


if __name__ == "__main__":
    main()