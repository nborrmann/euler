
import math

n=23
total=0

for n in range(1,101):
    for k in range(1,int(n/2)+1):
        k_fac=math.factorial(k)

        s=1
        for i in range(n-k+1,n+1):
            s*=i

        if(s>=k_fac*(10**6)):
            if(k==n/2):
                total+=1
            else:
                total+=2

print(total)