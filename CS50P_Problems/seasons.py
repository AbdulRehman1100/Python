from datetime import date, timedelta
import sys, inflect, re

def calculate_minutes(born):
        today_date = date.today()
        delta = today_date - born
        days = delta.days
        minutes = days * 24 * 60
        return minutes

def minutes_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


def main():
    birth_date_str = input("Date of Birth: ")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", birth_date_str):
            sys.exit("Invalid date")
    try:
        year, month, day = birth_date_str.split("-")
        born = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid date")
    minutes = calculate_minutes(born)
    print(minutes_to_words(minutes))

if __name__ == "__main__":
    main()