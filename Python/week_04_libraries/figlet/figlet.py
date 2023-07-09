from pyfiglet import Figlet
import sys
import random

def main():
    # check number of arguments passed
    num_args = len(sys.argv)

    # innitiate figlet
    figlet = Figlet()
    fonts = figlet.getFonts()

    # innitiate font for printing
    f = ""

    # no command-line arguments provided, print in random font
    if num_args == 1:
        # set a random index, to get a random font
        index = random.randint(0, len(fonts)-1)
        f = fonts[index]

    # command-line arguments provided, extract the desired font
    elif num_args == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # collects font from command line
        f = sys.argv[2]

        # checks if font is in list
        if f not in fonts:
            print("Invalid usage")
            sys.exit(1)
    else:
        # invalid number or format of command-line arguments
        print("Invalid usage")
        sys.exit(1)


    # collects string from user
    str = input("Say what? ")

    # set font and print text
    figlet.setFont(font=f)
    # print text
    print(figlet.renderText(str))



if __name__ == "__main__":
    main()