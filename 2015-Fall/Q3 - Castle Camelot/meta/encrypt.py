import sys


if __name__ == "__main__":

    

    lines = [l.strip() for l in sys.stdin.readlines()]
    newlines = []
    temp = []

    for n in range(0, len(lines[0])):
        for line in lines:
            temp.append(line[n])
        newlines.append(temp)
