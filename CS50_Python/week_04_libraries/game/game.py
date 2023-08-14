#import random and sys library
import random
import sys

def main():
    # gets the level the user wants to play, sends text for prompt
    l = get_input("Level: ")
    # generates a random number
    g = random.randint(0, int(l)+1)
    # calls function for user to guess g
    guess(g)

def get_input(s):
    #prompts user to enter an integer
    while True:
        try:
            x = input(s)
            #checks if x is a postive integer
            if x.isdigit() and int(x) > 0:
                return(x)
        except Exception:
            continue

def guess(g):

    while True:
        try:
            # Gets values to be guesses
            x = get_input("Guess: ")
            x = int(x)

            if x < g:
                print("Too small!")
                raise Exception
            elif x > g:
                print("Too large!")
                raise Exception
            else:
                print("Just right!")
                sys.exit(1)

        except Exception:
            continue
        else:
            break

if __name__ == "__main__":
    main()