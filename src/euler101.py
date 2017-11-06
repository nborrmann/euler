from numpy import *
from scipy import *

a = array([1])
for i in range(2,11):
    a = append(a, 1-i+i**2-i**3+i**4-i**5+i**6-i**7+i**8-i**9+i**10)


M = arange(100, dtype=object).reshape(10, 10)

for i in range(0,10):
    for j in range(0,10):
        M[i][j] = (i+1)**(j)

solution = linalg.solve(M, a)
s = 0
for i in range(0,10):
    s+= int(solution[i])*10**i

print(s)

        
