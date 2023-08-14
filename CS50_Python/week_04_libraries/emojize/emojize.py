import emoji

def main():
    emoji_text()

def emoji_text():
    string = input("Say what? ")

    print(emoji.emojize(string))

if __name__ == "__main__":
    main()