import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"\"(https?://(www\.)?youtube.com/embed/\w+)\"",s)
    if match:
        reset, id = match.group(1).rsplit("/", 1)
        return "https://youtu.be/"+id
    return None

if __name__ == "__main__":
    main()