import math

c = 111111111

n = 0
k = 0
while ((k**2)*2.25<=c**2):
    l = math.sqrt(4/3*(c**2-(k**2)*2.25))
    if (l%2==k%2):
        if(l==0 or k==0):
            n+=2
        else:
            n+=4
        
    #print("k=%f, l=%f, n=%f"%(k,l,n))
    k+=1
