minFrac=[0,1000000]
maxFrac=3/7

for d in range(1,1000000):
    for n in range(int(minFrac[0]/minFrac[1]*d),int(maxFrac*d)+1):
        if(minFrac[0]/minFrac[1]<n/d<maxFrac):
            minFrac=[n,d]

print("%i/%i" % (minFrac[0], minFrac[1]))
