def main():
    n = int(input("What's n?"))

    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
    # the YIELD asays return one value at a time
        yield("🐑") * n 


if __name__ == "__main__":
    main()

    # CTRL + C stopts the programme from running