import sys

lines = [l.strip() for l in sys.stdin.readlines()]

for l in reversed(lines):
    print l
