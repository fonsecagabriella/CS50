import sys
import PIL
from PIL import Image
from PIL import ImageOps

def main():
    i_file, o_file = user_input()
    print(i_file + " " + o_file)
    wears_shirt(i_file, o_file)

def user_input():

    extentions = ["jpg", "jpeg", "png"]

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        input_f = sys.argv[1].lower()
        output_f = sys.argv[2].lower()
        if "." in input_f and "." in output_f:
            input_f_ext = input_f.split(".")[1]
            output_f_ext = output_f.split(".")[1]

            if output_f_ext not in extentions or input_f_ext not in extentions:
                print("Invalid input")
                sys.exit(1)
            elif not output_f_ext == input_f_ext:
                print("Input and output have different extensions")
                sys.exit(1)
            else:
                return input_f, output_f
        else:
            print("Invalid file format")
            sys.exit(1)

def wears_shirt(i_file, o_file):

    try:
        #innitialise shirt, by opening file
        shirt = Image.open("shirt.png")

        # innitialise person who will wear shirt, based on user input
        person = Image.open(i_file)

        # files need to be the same size for programme to run
        # we resize person to fit the shirt following instruction from assignment
        # pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
        new_puppet = ImageOps.fit(person, shirt.size, bleed=0.0, centering=(0.5, 0.5))

        # pastes shirt in the person
        new_puppet.paste(shirt, mask=shirt)
        # saves as desired o_file
        new_puppet.save(o_file)

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

    except PIL.UnidentifiedImageError:
        print("Error manipulating images")
        sys.exit(1)


if __name__ == "__main__":
    main()