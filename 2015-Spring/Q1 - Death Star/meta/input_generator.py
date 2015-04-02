# input_generator.py for Q1 by Andrew Sosa
import random, sys
terms = int(sys.argv[1])
operans = [" + "," + ", " + ", " - ",  " - ",  " - ", " * ", " * ", " * ", " / ", " / "]
result = ""
for i in range(1, terms):
    result = result + str(random.randint(1, 9)) + random.choice(operans)
print result[:-3]
