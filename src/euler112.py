from datetime import datetime

def isBouncy(n, incr=-1):
    j = n%10
    n = int(n/10)
    
    if (incr == -1):
        if (j<n%10):
            incr = 0
        if (j>n%10):
            incr = 1
    if (n == 0):
        return False
            
    if (j > n%10 and incr==0):
        return True
    if (j < n%10 and incr==1):
        return True
    
    return isBouncy(n, incr)
    
    
a = datetime.now()
bouncy = 0
i = 1
while True:
    if isBouncy(i):
        bouncy += 1        

    if (bouncy*100 >= 99*i):
        print(i)
        break
    i+=1
    
b = datetime.now()
c=b-a
print(c.seconds, c.microseconds)
