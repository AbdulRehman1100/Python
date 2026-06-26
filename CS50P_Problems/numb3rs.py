import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if match:
        for group in match.groups():
            if not (0 <= int(group) <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()