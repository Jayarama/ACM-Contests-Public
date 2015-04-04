# garbage_compactor.py by Andrew Sosa
import sys, string

def sort_line(line, result = "["):

    # Filter all non alphabetic characters.
    characters = [x for x in line if x in string.ascii_letters]

    # Grab all "backs" of pairs
    backs = [characters[i] for i in range(1, len(characters), 2)]

    # Identify index of starting unique character
    index = characters.index(next(x for x in characters if x not in backs))

    # Add formatted results for each index lookup
    for i in range(0, len(backs)):
        result = result + "[" + characters[index] + ", " + characters[index + 1] + "],"
        index = next((x for x in range(0, len(characters)) if x != (index + 1) and characters[x] == characters[index + 1]), 0)

    # Print formatted result
    print result.rstrip(",") + "]"

# Read all the input with cleaned the newlines, and print the "sorted" form
[sort_line(l) for l in [l.strip() for l in sys.stdin.readlines()]]
