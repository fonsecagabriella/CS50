import random

def main():
    # get level from user
    level = get_level()

    # innitiates score
    score = 0


    # user plays 10 rounds
    for i in range(10):

        # for each round, generate x, y and resets tentatives
        x = generate_integer(level)
        y = generate_integer(level)
        tent = 0

        # give 3 tentatives to score
        while tent < 3:
            if check_math(x,y):
                score +=1
                break
            tent += 1
        # if doesn't answer right, gives answer
        if tent == 3:
            print(f"{x} + {y} = {x+y}")

    #prints final score
    print(f"Score: {score}")






def get_level():
    while True:
        try:
            level = input("Level: ")

            if int(level) not in [1, 2, 3]:
                raise Exception
        except (ValueError, Exception):
            continue

        return level

def check_math(x,y):
    while True:
        try:
            # get user input
            z = input(f"{x} + {y} = ")

            if int(z) == x + y:
                return True
            else:
                print("EEE")
                return False

        except ValueError:
            # if the value input by user is not valid, prints EEE
            print("EEE")
            return False


def generate_integer(level):
# returns integer based on used level
    match(level):
        case "1":
            return random.randint(0, 10)
        case "2":
            return random.randint(10, 100)
        case "3":
            return random.randint(100, 1000)


if __name__ == "__main__":
    main()