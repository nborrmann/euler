
def threeConsecutive(i):
    count = 1
    j=-1
    while True:
        if (i%10 == j):
            count+=1
        else:
            count=1
        j = i%10
        i = int(i/10)
        if (count==3):
            return True
        if (i==0):
            return False


i=1
n=0.0
while (i<10**12):
    if(not threeConsecutive(i)):
        n+=1/i
    i+=1

print(n)
