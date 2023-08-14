menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    get_items()


def get_items():
    total_price = 0
    item_price = 0

    while True:
        try:
            item = input("Item: ")
            item = format_item_name(item)
            item_price = menu[item]

            total_price += item_price
            print(f"${total_price:.2f}")
        except KeyError:
            continue
        except EOFError:
            break



def format_item_name(item):
    words_in_item = item.split()

    #renew item
    item=""

    for word in words_in_item:
        item = item + word.capitalize() + " "

    item = item.strip()
    return item

if __name__ == "__main__":
    main()