# Python3 sample solution for Q4 - Pirates
# By Preston Hamlin

from sys import stdin, stdout
from collections import deque

DEBUG = False
# DEBUG = True


# stores all potential start locations
start_locations = []
treasure_locations = set()
q = deque()


# get everything from the input file via stdin
data = stdin.readlines()
map_dim, num_instr = [int(x) for x in data[0].split()]
if DEBUG:
    print(map_dim, num_instr)

# parse the map and instructions
treasure_map = [line.strip().split() for line in data[1 : map_dim+1]]
instructions = [line.strip().split() for line in data[map_dim+1 : map_dim+num_instr+1]]
for i in instructions:
    i[2] = int(i[2])
    
if DEBUG:
    print("\nmap:")
    for col in treasure_map:
        print(col)
    print(instructions)

# determine potential start locations
for y, col in enumerate(treasure_map):
    for x, val in enumerate(col):
        if val == '0':
            start_locations.append((x,y))

if DEBUG:
    print("\nstart locations:")
    for loc in start_locations:
        print(loc)



# searches in cardinal directions from provided location for landmark
def FindLandmark(landmark, loc):
    if DEBUG:
        print("searching for landmark {} from loc {}".format(landmark, loc))
    ret = []
    # search horizontally from location
    for x in range(map_dim):
        if treasure_map[loc[1]][x] == landmark:
            ret.append( (x,loc[1]) )

    # search vertically from direction
    for y in range(map_dim):
        if treasure_map[y][loc[0]] == landmark:
            ret.append( (loc[0],y) )
    return ret



# returns modified coordinates after moving in a cardinal direction
def ApplyCardinalMove(loc, direction, distance):
    ret_x = loc[0]
    ret_y = loc[1]
    if direction == 'N':
        ret_y -= distance
    elif direction == 'S':
        ret_y += distance
    elif direction == 'E':
        ret_x += distance
    elif direction == 'W':
        ret_x -= distance
    else:
        if DEBUG:
            print("ERROR: unknown direction")
        return
    return (ret_x, ret_y)


# checks if coordinates are valid
def ValidCoord(loc):
    for coord in loc:
        if coord < 0 or coord >= map_dim:
            return False
    return True


# creates a list of all the child productions based on location and instruction
def GetChildren(loc, instruction):
    if DEBUG:
        print("finding children for {} based on {}".format(loc, instruction))
    ret = []
    
    next_landmark, next_card, next_dist = instruction
    found_landmarks = FindLandmark(next_landmark, loc)
    for landmark in found_landmarks:
        modified = ApplyCardinalMove(landmark, next_card, next_dist)
        if ValidCoord(modified):
            ret.append(modified)

    return ret


for loc in start_locations:
    q.append( (loc,0) )



# start BFS to follow paths
while len(q) != 0:
    if DEBUG:
        print()
        print(q)
    popped = q.popleft()
    
    if DEBUG:
        print("    popped {}".format(popped))
        
    loc, inst = popped
    if inst >= num_instr:
        #treasure_locations.add(popped)
        treasure_locations.add(loc)
        continue
    
    children = GetChildren(loc, instructions[inst])
    if DEBUG:
        print("    children: \n{}".format(children))
    for child in children:
        q.append( (child,popped[1]+1) )



#print("\ntreasure locations: \n{}".format(treasure_locations))
for loc in treasure_locations:
    stdout.write("{} ".format(loc))
stdout.write("\n")

# TODO: BFS to find treasure
