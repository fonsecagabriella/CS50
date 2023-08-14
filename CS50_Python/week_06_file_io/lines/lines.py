import sys

def main():
    f = get_file_name()
    count= read_and_count(f)
    print(count)

def get_file_name():

    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print ("Too many command-line arguments")
        sys.exit(1)
    else:
        return sys.argv[1]

def read_and_count(file):
    # count lines
    i = 0
    # counts comments
    comments = 0
    # counts blank
    blank_l = 0

    try:
        if not file.endswith(".py"):
            print("Not a Python file")
            sys.exit(1)
        else:
            with open(file) as f:
                for line in f:
                    line = line.strip()
                    if not line.startswith("#") and not line == "":
                        i += 1
                    if line.startswith("#"):
                        comments += 1
                    if line.strip() == "":
                        blank_l += 1

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    return i




if __name__ == "__main__":
    main()