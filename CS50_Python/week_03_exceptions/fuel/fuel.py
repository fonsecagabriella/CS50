def main():
    f = get_fraction()
    tank_message(f)

def get_fraction():
    # this programme will loop forever until user inputs integers for both x and y
    x, y, tank_percent = "", "", ""

    while True:
        try:
            x,y  = input("What is the fraction? ").split("/")
            tank_percent = int(x)/int(y)
            check_tank_ratio(int(x), int(y))
        except (ValueError, ZeroDivisionError, ExceptionXmoreThanY):
            continue
        else:
            break

    return tank_percent

def tank_message(tank_percent):
    if tank_percent <= 0.01:
        print("E")
    elif tank_percent >= 0.99:
        print("F")
    else:
        print(f"{round(tank_percent*100)}%")

# the class and function below are a custom exception to check if
# the tank has more gas than it is allowed
class ExceptionXmoreThanY(Exception):
    pass

def check_tank_ratio(x, y):
    if x >y:
        raise ExceptionXmoreThanY


if __name__=="__main__":
    main()