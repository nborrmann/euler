dim=7

def sum_digits_squared(n):
    s = 0
    while n:
        s+=(n%10)**2
        n//=10
    return(s)

#fill cache
cachesize = 81*dim
cache=[False]*cachesize
for n in range(1,cachesize):
    i=n
    while 1:
        if (i==89):
            cache[n-1]=True
            break
        elif(i==1):
            break
        i=sum_digits_squared(i)

count=0
for n in range(1,10**dim):
    if (cache[sum_digits_squared(n)-1]):
        count+=1

print(count)
