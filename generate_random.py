# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)
# test

import random

cards = ["jack", "queen",  "king"]
random.shuffle(cards)
for card in cards:
    print(card)
