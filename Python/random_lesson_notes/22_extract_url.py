import re
url = input("what's your Twitter? ").strip()

# find and replace function
# username = url.replace("https://twitter.com/", "")
# print(url)

# username = url.removeprefix(prefix)

# substitute function
# this is find and replace using regular expressions

#username = re.sub(r"^https?://(www\.)*twitter\.com/", " ", url)
#print(username)

# notice when you use ^ you need to use a space after hitting the key otherwise
# you have ˆ which is small

if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/([a-z0-9_]+)", "", url, re.IGNORECASE):
    # note we can use group 1 because the first group has ?:
    # which means do not capture
    print(f"Username is ", matches.group(1))