months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December" ]


def main():
    get_date()

def check_format(date):
    if "/" in date or "," in date:
        if "/" in date:
            m, y, d = date.split("/")
            return 1<= int(m) <=12
    else:
        raise ExceptionIsDate



def format_date(date):
    date = date.replace("/", " ").replace(",", "").strip()
    return date

def get_date():

    while True:
        try:
            date = input("Date: ")

            check_format(date)

            # formats user entry
            date = format_date(date)

            # check if date is valid
            if (is_valid(date)):
                print_date(date)
            else:
                raise ExceptionIsDate
        except (ExceptionIsDate, ValueError):
            continue
        except EOFError:
            break
        else:
            break

def print_date(date):
    m, d, y = date.split(" ")

    if m in months:
        m = month_number(m)

    m = int(m)
    d = int(d)

    print(f"{y}-{m:02}-{d:02}")


def is_valid(date):
    m, d, y = date.split(" ")
    return is_month_valid(m) and is_day_valid(d) and is_year_valid(y)


def is_month_valid(m):
    return  (m in months) or 1<= int(m) <=12


def is_day_valid(d):
    return 1 <= int(d) <= 31


def is_year_valid(y):
    return len(y) == 4


def month_number(m):
    calendar = [
    {"month_name": "January", "month_number": 1, "days": 31},
    {"month_name": "February", "month_number": 2, "days": 28},
    {"month_name": "March", "month_number": 3, "days": 31},
    {"month_name": "April", "month_number": 4, "days": 30},
    {"month_name": "May", "month_number": 5, "days": 31},
    {"month_name": "June", "month_number": 6, "days": 30},
    {"month_name": "July", "month_number": 7, "days": 31},
    {"month_name": "August", "month_number": 8, "days": 31},
    {"month_name": "September", "month_number": 9, "days": 30},
    {"month_name": "October", "month_number": 10, "days": 31},
    {"month_name": "November", "month_number": 11, "days": 30},
    {"month_name": "December", "month_number": 12, "days": 31}
    ]

    for month in calendar:
        if month["month_name"] == m:
            return month["month_number"]


# the class and function below are a custom exception to check if
# user entry is date
class ExceptionIsDate(Exception):
    pass


if __name__ == "__main__":
    main()