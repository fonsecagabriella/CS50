import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # removes any spaces before and after
    ip = ip.strip()

    # checks if input is in ip format
    if bool(re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip)):
        # if so, check if digits are between 0-255
        digits = ip.split(".")


        for d in digits:
            if 0 <= int(d) <= 255:
                continue
            else:
                return False
        return True
    # else returns false
    else:
        return False


def validate1(ip):
    # removes any spaces before and after
    ip = ip.strip()

    # checks if input is in ip format
    if is_ip_format(ip):
        # if so, check if digits are between 0-255
        return valid_digits(ip)
    # else returns false
    else:
        return False

def valid_digits(ip):
    digits = ip.split(".")

    for d in digits:
        if 0 <= int(d) <= 255:
            continue
        else:
            return False

    # if the programme run until here, returns True
    return True


def is_ip_format(ip):
    # check if IP format using REGEX
    return bool(re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip))


if __name__ == "__main__":
    main()