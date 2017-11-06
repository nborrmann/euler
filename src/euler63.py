
import math

c=0
n=1
lower=0

while(lower<10):
    lower = math.ceil(10**((n-1)/n))
    n+=1
    c+=(10-lower)

print(c)


l = sum([10-math.ceil(10**((n-1)/n)) for n in range(1,22)])




