#Using library re for regex

import re

email = input("What's your email?").strip()

"""
if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
"""

# quick regex reference
#.          any character except a new line
#*          0 or more repetitions
#+          1 or more repetitions
#?           0 or 1 repetition
#{m}a        m repetitions of a
#{m, n}      m to n repetitions
#\x         tells you want character x
# ^         matches the start of string
#$          matches the end of the string
#[abc]     set of characters (only abc)
#[^x]       complementing the set (any caracter except x)
# a-z       a to z, need to do for caps too
# \d        decimal digit
# \D        not decimal
# \s        whitespace characters
# \S        not whitespace
# \w        word character as well as number and underscore
# \W        not a word character
# A|B       either A or B
# (...)     a group, doesn't do anything. you put the sign in the end
# (?:...)   non-capturing version



# Example
# [a-zA-Z0-9_] letters, numbers, underscores

# (a-z_)?       letters and underscores, can appear or not - because of the ?


# the r tells python to interprate the input as a raw string, ie \n doesnt become breakline
# following code not useful because user can add more stuff to the beginning or
#  end, like a full sentence
#if re.search(r".+@.+\.edu", email):
#    print("Valid")
#else:
#    print("Invalid")


# flags you can use
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL


# anything to the left of right cannot have @
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


"""
[a-zA-Z0-9_] this means the user can input a to z, numbers and _

"""