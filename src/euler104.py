import math
from datetime import datetime

n = 1234546789234211234564789

def is_pandigital_bit(n):
    print(n)
    digits = 0
    count = 0
    tmp = 0

    while (n > 0):
        tmp = digits;
        digits = digits | 1 << (n - ((n // 10) * 10) - 1)
        if (tmp == digits):
            return False

        count += 1
        n //= 10

    return digits == (1 << count) - 1


def is_pandigital(n):
    dim=int(math.log10(n))+1
    if not is_pandigital_bit(n%10**10):
        return false
    if not is_pandigital_bit(int(n/10**(dim-9))):
        return false
    return true

is_pandigital_bit(1534398)
f0=0
f1=1
k=1
while 1:
    k+=1
    f0, f1 = f1, f0+f1
    if (is_pandigital(f1)):
        print(k)
        break


#print(is_pandigital(n))
























