import sys

import argparse


# argparse is a library that allows users to pass commands via command line

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, 
                    help="number of times to meow", type=int)

args = parser.parse_args()


for _ in range(int(args.n)):
    print("meow")


# Run in command line
# 36_ArgParse.py -n 5
# to make the cat meow

# if you use
# programma.py h
# you get options 