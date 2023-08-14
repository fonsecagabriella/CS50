def main():
    t = input("What time is it? ")
    meal(t)


def convert(time):
    x, y = time.split(":")

    if y.endswith("am") or y.endswith("pm"):
        y, z = y.split()
        if z == "pm":
            x = int(x) + 12

    return float((int(x)*60 + int(y))/60)

def meal(time):
    #converts time from string to float
    time = convert(time)

    if  7 <= time <=8:
        print ("breakfast time")
    elif 12 <= time <=13:
        print ("lunch time")
    elif 18 <= time <=19:
        print ("dinner time")

if __name__ == "__main__":
    main()