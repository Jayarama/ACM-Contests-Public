# Python3 sample solution for Q4 - Pirates

from sys import stdin
from collections import deque

# stores all potential start locations
start_locations = []
q = deque()


# get everything from the input file via stdin
data = stdin.readlines()
map_dim, num_instr = [int(x) for x in data[0].split()]
print(map_dim, num_instr)

# parse the map and instructions
treasure_map = [line.strip().split() for line in data[1 : map_dim+1]]
instructions = [line.strip().split() for line in data[map_dim+1 : map_dim+num_instr+1]]
print("\nmap:")
for col in treasure_map:
    print(col)
print(instructions)

# determine potential start locations
for y, col in enumerate(treasure_map):
    for x, val in enumerate(col):
        if val == '0':
            start_locations.append((x,y))

print("\nstart locations:")
for loc in start_locations:
    print(loc)

# TODO: BFS to find treasure
