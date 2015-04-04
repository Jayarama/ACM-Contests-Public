# Python3 solution for S2015 Q2
# By Preston Hamlin

from sys import stdin, stdout

for line in stdin.readlines():
  by_first, by_second, ret = {}, {}, "["
  for index in [i for i,j in enumerate(line[1:]) if j=='[']:
    by_first[line[index+2]], by_second[line[index+5]]  =  (line[index+2],line[index+5]), (line[index+2],line[index+5])

  start, end = list( set(by_first.keys()) - set(by_second.keys()) ) [0],  list( set(by_second.keys()) - set(by_first.keys()) ) [0]
  while start != end:
    ret, start = ret + ("[{}, {}], ".format(by_first[start][0], by_first[start][1])),  by_first[start][1]
      
  print(ret[:-2] + ']')
