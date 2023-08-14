import statistics
import random
import sys

x= random.randint(1, 100)
y= random.randint(1, 100)
print(statistics.mean([x, y]))
print(f"x was {x} and y was {y}")


print("hello, my name is", sys.argv[0])