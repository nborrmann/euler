import math

pairs = [[int(n) for n in line.strip().split(',')] for line in open("euler100.txt", "r")]
print (max([(pair[1]*math.log(pair[0]),i+1) for (i,pair) in enumerate(pairs)]))
