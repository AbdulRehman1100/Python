import re

def main():
    print(convert(input("Hours: ")))

def validate_hour(hour):
    if 1 <= int(hour) <= 12:
        return True
    return False

def convert_time(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0
    if not validate_hour(hour):
        raise ValueError
    if period == "AM":
        hour = 0 if hour == 12 else hour
    elif period == "PM":
        hour = 12 if hour == 12 else hour + 12
    return f"{hour:02d}:{minute:02d}"


def convert(s):
    if match := re.match(r"(^1?[0-9])(?::([0-5][0-9]))? (AM|PM) to (1?[0-9])(?::([0-5][0-9]))? (AM|PM)$", s):
        time1 = convert_time(match.group(1), match.group(2), match.group(3))
        time2 = convert_time(match.group(4), match.group(5), match.group(6))
        return f"{time1} to {time2}"
    else:
        raise ValueError
    

if __name__ == "__main__":
    main()