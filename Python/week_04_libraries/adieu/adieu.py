def main():
    adieu()

def adieu():
    list_names = list()

    while True:
        try:
            name = input("Name: " )
            list_names.append(name)
        except EOFError:
                print("\n")
                print_adieu(list_names)
                break

def print_adieu(names):
    str_to_print = "Adieu, adieu, to "

    i = 0

    while i < len(names):
        if len(names) == 1:
             str_to_print = str_to_print + names[0]
        elif len(names) == 2:
             str_to_print = str_to_print + names[0] + " and " + names[1]
             i = len(names)*2 
        elif i == len(names) - 1:
             str_to_print = str_to_print+ "and " + names [i]
        else:
            str_to_print = str_to_print + names[i] + ", "

        i += 1

    print(str_to_print)


if __name__ == "__main__":
     main()


