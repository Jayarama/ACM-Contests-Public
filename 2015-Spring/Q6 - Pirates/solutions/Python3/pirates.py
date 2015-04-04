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
    i[2] = int(i[2]) if i[2].isdigit() else -1
    
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
        print("    searching for landmark {} from loc {}".format(landmark, loc))
    ret = []
    
    # if known search item, search for it
    if landmark != 'X':
        # search horizontally from location
        for x in range(map_dim):
            if treasure_map[loc[1]][x] == landmark:
                ret.append( (x,loc[1]) )
    
        # search vertically from direction
        for y in range(map_dim):
            if treasure_map[y][loc[0]] == landmark:
                ret.append( (loc[0],y) )
    # otherwise get all landmarks
    else:
        # search horizontally from location
        for x in range(map_dim):
            if treasure_map[loc[1]][x] != '-':
                ret.append( (x,loc[1]) )
    
        # search vertically from direction
        for y in range(map_dim):
            if treasure_map[y][loc[0]] != '-':
                ret.append( (loc[0],y) )
    return ret



# returns modified coordinates after moving in a cardinal direction
def ApplyCardinalMove(loc, direction, distance):
    # ret_x = loc[0]
    # ret_y = loc[1]
    ret = []
    
    # create a list of all possible directions to move in
    dirs = ['N', 'S', 'E', 'W'] if direction == 'X' else [direction]
    
    # create a list of all possible distances to travel
    dist = range(map_dim) if distance == -1 else [distance]
    
    # for all possible combinations of direction and distance, find a point
    for d1 in dirs:
        for d2 in dist:
            ret_x = loc[0]
            ret_y = loc[1]
    
            if d1 == 'N':
                ret_y -= d2
            elif d1 == 'S':
                ret_y += d2
            elif d1 == 'E':
                ret_x += d2
            elif d1 == 'W':
                ret_x -= d2
            else:
                if DEBUG:
                    print("ERROR: unknown direction")
                return ret
                
            ret.append( (ret_x, ret_y) )
    return ret


# checks if coordinates are valid
def ValidCoord(loc):
    for coord in loc:
        if coord < 0 or coord >= map_dim:
            return False
    return True


# creates a list of all the child productions based on location and instruction
def GetChildren(loc, instruction):
    if DEBUG:
        print("    finding children for {} based on {}".format(loc, instruction))
    ret = []
    
    next_landmark, next_card, next_dist = instruction
    
    # get all visible and applicable landmarks 
    found_landmarks = FindLandmark(next_landmark, loc)
    
    
    for landmark in found_landmarks:
        modified = ApplyCardinalMove(landmark, next_card, next_dist)
        
        for m in modified:
            if ValidCoord(m):
                ret.append(m)

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
        print("children: \n{}".format(children))
    for child in children:
        e = (child,popped[1]+1)
        if e not in q:
            q.append( e )



#print("\ntreasure locations: \n{}".format(treasure_locations))
for loc in sorted(treasure_locations):
    stdout.write("{} ".format(loc))
stdout.write("\n")
