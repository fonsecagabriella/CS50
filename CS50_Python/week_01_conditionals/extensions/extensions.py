def main():
    user_file()

def user_file():
    file_name = input("What is your file name? ")
    file_name = format_string(file_name)
    file_type(file_name)

def format_string(s):
    return s.strip().lower()

def file_type(f):
    if f.endswith(".gif"):
        return print("image/gif")
    elif f.endswith(".jpg"):
        return print ("image/jpeg")
    elif f.endswith(".jpeg"):
        return print ("image/jpeg")
    elif f.endswith(".png"):
        return print("image/png")
    elif f.endswith(".pdf"):
        return print("application/pdf")
    elif f.endswith(".txt"):
        return print("text/plain")
    elif f.endswith(".zip"):
        return print("application/zip")
    else:
        return print("application/octet-stream")


if __name__ == "__main__":
    main()