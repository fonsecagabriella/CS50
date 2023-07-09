def main():
    s = to_snake(input("Input your camelCase variable: "))

def to_snake(var_camel):
    snake = ""

    for letter in var_camel:
        if letter.isupper():
            snake = snake + "_" + letter.lower()
        else:
            snake = snake + letter

    print(snake)


if __name__ == "__main__":
    main()