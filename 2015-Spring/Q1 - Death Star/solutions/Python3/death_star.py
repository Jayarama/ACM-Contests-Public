# Python3 solution for S2015 Q1
# By Preston Hamlin

from sys import stdin


def PairGenerator(stuff):
  for i in range(0, len(stuff), 2):
    try:
      yield (stuff[i], stuff[i+1])
    except IndexError:
      yield None


contents = stdin.read().strip().split()
total = int(contents.pop(0))

def AddFunc(val):
  global total
  total += val
def SubFunc(val):
  global total
  total -= val
def MulFunc(val):
  global total
  total *= val
def DivFunc(val):
  global total
  total = int(total / val)

opmap = {
  '+' : AddFunc,
  '-' : SubFunc,
  '*' : MulFunc,
  '/' : DivFunc
}


for pair in PairGenerator(contents):
  opmap[pair[0]](int(pair[1]))
  #print("{} {}  -->  {}".format(pair[0], pair[1], total))
  
print(total)
