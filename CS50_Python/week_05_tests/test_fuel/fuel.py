import sys
import pytest

def main():
    fraction = input("What is the fraction? ")

    percentage = convert(fraction)



def convert(fraction):
    # this programme will loop forever until user inputs integers for both x and y
    x, y, tank_percent = "", "", ""

    while True:
        try:
            x,y  = fraction.split("/")

            if int(x) > int (y):
                raise ValueError

            if int(y) == 0:
                raise ZeroDivisionError

            tank_percent = int(x)/int(y)

        except (ValueError, ZeroDivisionError):
            #sys.exit(1)
            fraction = input("What is the fraction? ")
            convert(fraction)
            break
        else:
            break

    return (round(tank_percent*100))


def gauge(percentage):
    if int(percentage) <= 1:
        return "E"
    elif int(percentage) >= 99:
        return "F"
    else:
        return str(percentage) + "%"



if __name__=="__main__":
    main()