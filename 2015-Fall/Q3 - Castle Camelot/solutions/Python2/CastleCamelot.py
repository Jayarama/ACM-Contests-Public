import sys
def p(s):
    print s
[p(l[::-1]) for l in [l.strip() for l in sys.stdin.readlines()]]
