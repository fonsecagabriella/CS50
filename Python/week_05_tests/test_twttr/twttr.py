def main():
    tweet = shorten(input("Give me your Tweet: "))
    print(tweet)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u",
           "A", "E", "I", "O", "U"]
    tweet = ""
    for l in word:
        if l not in vowels:
            tweet += l
    return(tweet)


if __name__ == "__main__":
    main()