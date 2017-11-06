from math import factorial as fac
from PIL import Image
import math
from datetime import datetime

lines = 98
img = Image.new( 'RGB', (lines,lines), "white")
pixels = img.load()

def sevensInNumber(n):
    total = 0
    c=1
    while c>0:
        c = n//7
        total+=c
        n=c
    return total

#print(sevensInNumber(8))


def sevensInRow(n):
    counter=0
    for k in range(0,n+1):
        if (sevensInNumber(n) > sevensInNumber(n-k)+sevensInNumber(k)):
            counter+=1
            pixels[k,n]=(100,100,100) #(lines-n)/2+
        #else:
            #s+=" - "
    #print(n,counter)
    return(counter)

def sevensInRowStupid(n):
    counter=0
    for k in range(0,n+1):
        f = fac(n)//(fac(n-k)*fac(k))
        #print(n,k,n-k, f, f%7 == 0, n//7 > (n-k)//7+k//7)
        if (f%7 == 0):
            counter+=1
    #print(n, counter)
    return(counter)

hundredSum = 0
for n in range(lines):
    hundredSum += sevensInRow(n)

#print(5050-hundredSum)

img.show()
print("***************************")

def base_conv(n):
    b7 = ''
    while n>0:
        b7 += str(n%7)
        n//=7
    return(b7[::-1])

def calc(n_base7):
    res = 0
    for n in n_base7:
        res += int(n)*(res+1)
    return(res)

#print(calc(base_conv(20)))

def calc_product(n):
    res=1
    while n>0:
        div = divmod(n,7)
        res*=(div[1]+1)
        n=div[0]
    return res


startTime = datetime.now()
result=0
for i in range(0,10**7):
    result += calc_product(i)
    #print(i, i-sevensInRow(i), calc(base_conv(i)))
    #result+= calc(base_conv(i))
    #base_conv(i)

print(result)
print(datetime.now()-startTime)


"""
from math import trunc,log
f = lambda filas : trunc(log(filas,7))
g = lambda filas : trunc(filas/7**f(filas))
#filas,count,mult,r =  10**9,0,1,[1,3,6,10,15,21,28]
filas = 10**9
count=0
mult=1
r=[1,3,6,10,15,21,28]
while filas >= 7:
    count += mult*r[g(filas)-1]*28**f(filas)
    mult *= g(filas)+1
    filas -= g(filas)*7**f(filas)
count += mult*r[filas-1] #Ajusta la última iteración a mano
print(count)
"""
