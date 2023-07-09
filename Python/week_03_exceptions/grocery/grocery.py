def main():
    groceries = get_items()
    shopping_list(groceries)


def get_items():
    groceries = list()

    while True:
        try:
            item = input()
            groceries.append(item.upper())
        except EOFError:
            break

    return groceries


def shopping_list(groceries):
    counts = {}

    for item in groceries:
        counts[item] = groceries.count(item)

    for i in sorted(counts):
        print(f"{counts[i]} {i}")


if __name__ == "__main__":
    main()
