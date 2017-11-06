import math

f_10 = (1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
def sum_digits(n):
    r = 0
    while n:
        r,n = r +f_10[n % 10], n//10
    return(r)

cache={}
c=0

for n in range(10**6):
    l=[n]
    while 1:
        fac_digits = sum_digits(l[-1])
        if(fac_digits in l):
            for i in range(len(l)):
                cache[l[i]] = len(l)-i
            break

        l.append(fac_digits)

    if (len(l)==60):
        c+=1


print(c)














