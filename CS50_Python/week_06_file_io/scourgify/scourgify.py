import sys
from tabulate import tabulate
import csv

# USEFUL: Download file to folder via terminal
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv


def main():
    f = get_file_name()
    students = read(f)
    write(students)

def get_file_name():

    if len(sys.argv) <= 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print ("Too many command-line arguments")
        sys.exit(1)
    else:
        if sys.argv[1].endswith(".csv"):
            return sys.argv[1]
        else:
            print("Not a CSV file")
            sys.exit(1)

def read(file):
    students = []

    try:
        # open and read file
        with open(file) as f:
            reader = csv.DictReader(f)
            # for each row in the file reads name
            for row in reader:
                # splits name in first and last using ,
                last, first = row["name"].split(",")
                # creates a dic for student
                student = {"first": first.strip(), "last": last.strip(), "house": row["house"] }
                # appends to list
                students.append(student)

    except FileNotFoundError:
        # if specified reading file does not exist, returns error
        print("Could not read " + file)
        sys.exit(1)

    return students

def write(list_students):

    # gets the name of the file
    write_file = sys.argv[2]

    # open file for writing
    with open(write_file, "w", newline="") as csvfile:
        # creates the header
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # for each student in the list, write a row in the file
        for student in list_students:
            writer.writerow({
                "first" : student["first"],
                "last": student["last"],
                "house": student["house"]
            })

def read_and_print(file):
    try:
        if not file.endswith(".csv"):
            print("Not a CSV file")
            sys.exit(1)
        else:
            with open(file, newline="") as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Extract the headers
                table = [row for row in reader]  # Extract the rows
                print(tabulate(table, headers, tablefmt="grid"))
            sys.exit(0)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)




if __name__ == "__main__":
    main()