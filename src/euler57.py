from datetime import datetime
startTime = datetime.now()

def frac0(x):
    return((x[0] + x[1], x[0]))

def frac(x):
    return((2*x[0] + x[1], x[0]))


c=0
x=(2,1)
for i in range(1001):
    x0=frac0(x)
    if(len(str(x0[0]))>len(str(x0[1]))):
        c+=1

    x=frac(x)


print(c)


print(datetime.now()-startTime)




