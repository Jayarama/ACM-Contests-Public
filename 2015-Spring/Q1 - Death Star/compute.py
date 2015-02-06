# compute.py by Andrew Sosa

# This will handle stdin for us
import fileinput

# This list will hold the lines
lines = []

# Get all our lines
for line in fileinput.input():
    line = line.strip('\n')
    line = line.split()
    lines.append(line)

# This will compute values
def comp(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "/":
        return a / b
    if op == "*":
        return a * b
    else:
        return a

# This will evaluate a line
def eval(line):
    sum = int(line.pop(0))
    op = "+"
    for s in line:
        if s.isdigit():
            sum = comp(sum, int(s), op)
        else:
            op = s
    print sum

# Handle the things
for line in lines:
    eval(line)
