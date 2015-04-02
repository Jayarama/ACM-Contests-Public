# garbage_compactor.py by Andrew Sosa
import sys
import string

def sort_line(line):
    characters, fronts, backs, result = [], [], [], "["

    # Filter all non alphabetic characters.
    characters = [x for x in line if x in string.ascii_letters]

    # Grab fronts and backs
    bool = True
    for ch in characters:
        if bool:
            fronts.append(ch)
        else:
            backs.append(ch)
        # Flip bool
        bool = bool == False

    # Identify index of starting unique character
    index = characters.index(next(x for x in fronts if x not in backs))

    # Add formatted results for each index lookup
    for i in range(0, len(fronts)):
        result = result + "[" + characters[index] + ", " + characters[index + 1] + "],"
        if i < len(fronts) - 1:
            index = next(x for x in range(0, len(characters)) if x != (index + 1) and characters[x] == characters[index + 1])

    # Print formatted result
    print result.rstrip(",") + "]"

# Read all the input
lines = sys.stdin.readlines()

# Clean the newlines
lines = [l.strip() for l in lines]

# Process for each line
[sort_line(l) for l in lines]
