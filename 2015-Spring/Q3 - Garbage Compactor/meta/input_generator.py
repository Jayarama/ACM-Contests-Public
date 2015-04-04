# Generates random input
import string
import random
from random import shuffle


#w = int(raw_input("How many sets to create: "))
w = int(raw_input())

for ii in range(0, w):

    #x = int(raw_input("How many characters to use: "))
    x = int(raw_input())

    letters = []

    for i in range(0, (x)):
        ch = random.choice(string.ascii_lowercase)
        while ch in letters:
            ch = random.choice(string.ascii_lowercase)
        letters.append(ch)

    pairings = []

    for i in range(0, len(letters) - 1):
        temp = []
        temp.append(letters[i])
        temp.append(letters[i+1])
        pairings.append(str(temp))

    #print pairings

    # Save unshuffled copy
    y = str(pairings)

    # Shuffle the list
    shuffle(pairings)

    # This is our shuffled copy
    z = str(pairings)

    # Clean up both representations of the lists
    y = y.replace('\'', '')
    y = y.replace('\"', '')
    z = z.replace('\'', '')
    z = z.replace('\"', '')

    # Print both
    print y
    print z
