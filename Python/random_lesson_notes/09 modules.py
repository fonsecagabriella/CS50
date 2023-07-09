import random # explicitaly add 'from choice' if you want to use choice in the current namespace
                # no need to call as random.choice

""""
Example of a code that tosses coin
coin = random.choice(["heads", "tails"])
print(coin)
"""

# pick random number
#number = random.randint(1, 10)
#print(number)

cards = ["jack", "queen", "king", "A's heart"]
random.shuffle(cards)
for card in cards:
    print(card)
    