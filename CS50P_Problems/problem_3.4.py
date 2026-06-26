months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def print_date(year, month, day):
    print(f"{year}-{month:02d}-{day:02d}")

def is_valid_day(day):
    if 1 <= day <= 31:
        return True
    return False


while True:
    try:
        date = input("Date: ").strip()
        date_components = date.split("/")

        if len(date_components) == 3:
            month = int(date_components[0])
            if not 1 <= month <= 12:
                continue
            day = int(date_components[1])
            if not is_valid_day(day):
                continue
            year = int(date_components[2])
            print_date(year, month, day)
            break
        
        month, rest = date.split(" ", 1)
        day, year = rest.split(",", 1)
        year = year.strip()
        day = int(day)
        if not is_valid_day(day):
            continue
        if month not in months:
            continue
        month = months[month]
        print_date(year, month, day)
        break
    except:
        continue