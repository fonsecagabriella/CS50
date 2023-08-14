import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    # if result not None
    result = extract_hours_minutes(s)
    if result:
        # for legibility, assign values to variables
        start_hour, start_minute, start_ampm, end_hour, end_minute, end_ampm = result

        # check if values for hours are between 1 and 12
        if not 1 <= start_hour <= 12 or not 1<= end_hour <= 12:
            raise ValueError

        # check if values for minutes are between 0 and 59
        if not 0 <= start_minute <= 59 or not 0 <= end_minute <= 59:
            raise ValueError

        # formats start_hour to 24 format
        if start_ampm == "PM" and start_hour < 12:
            start_hour += 12

        # formats end_hour to 24 format
        if end_ampm == "PM" and end_hour < 12:
            end_hour += 12

        # treats case 12 AM = written as hour 0
        if start_ampm == "AM" and start_hour == 12:
            start_hour = 0

        # treats case 12 AM = written as hour 0
        if end_ampm == "AM" and end_hour == 12:
            end_hour = 0


        return (str(start_hour)).zfill(2) + ":" + (str(start_minute)).zfill(2) + " to " + (str(end_hour)).zfill(2) + ":" + (str(end_minute)).zfill(2)

    else:
        return "Invalid input"


def extract_hours_minutes(input_str):

    pattern = r"(\d+)(?::)?(\d+)? (AM|PM) to (\d+)(?::)?(\d+)? (AM|PM)"
    match = re.search(pattern, input_str)
    if match:
        start_hour = int(match.group(1))
        if match.group(2):
            start_minute = int(match.group(2))
        else:
            start_minute = 0
        start_ampm = match.group(3)
        end_hour = int(match.group(4))
        if match.group(5):
            end_minute = int(match.group(5))
        else:
            end_minute = 0
        end_ampm = match.group(6)
        return (start_hour, start_minute, start_ampm, end_hour, end_minute, end_ampm)
    else:
        raise ValueError



if __name__ == "__main__":
    main()