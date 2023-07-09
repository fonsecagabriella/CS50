# Get user string
user_string = input("Give me some text to play with: ")

# Remove excess space in begin and end of string
user_string = user_string.strip()

# Print user string with ...
print(user_string.replace(" ", "..."))