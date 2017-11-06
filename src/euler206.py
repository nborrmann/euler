import math
from datetime import datetime

maxValue = 1929394959697989990
minValue = 1020304050607080900
upper = int(math.sqrt(maxValue))
lower = int(math.sqrt(minValue))

compare = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def has_form_fancy(n):
    return [(n%10**i)//10**(i-1) for i in range(1,20,2)] == compare

def has_form(n):
    for i in range(10):
        if (n%10 != compare[i]):
            return False
        n//=10**2
    return True

def has_form_str(n):
    return str(n)[::2] == '1234567890'

##print(has_form_str(maxValue))
##print(has_form_str(minValue))
##print(has_form_str(1020304050607080901))

for i in range(lower,upper+1,10):
    if (has_form(i**2)):
        print(i, i**2)
        break


##lower=345234523*10**30
##startTime = datetime.now()
##for i in range(lower,lower+10**7,10):
##    if (has_form(i**2)):
##        print(i, i**2)
##        break
##print(datetime.now()-startTime)
##
##startTime = datetime.now()
##for i in range(lower,lower+10**7,10):
##    if (has_form_str(i**2)):
##        print(i, i**2)
##        break
##print(datetime.now()-startTime)

