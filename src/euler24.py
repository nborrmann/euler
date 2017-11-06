#problem #24
a=[0,1,2,3,4,5,6,7,8,9]
#a=[1,2,3,4]

def reverse(a):
    for k in range(len(a)-2,-1,-1):
        if (a[k]<a[k+1]):
            for l in range(len(a)-1,k,-1):
                if (a[k]<a[l]):
                    a[k],a[l]=a[l],a[k]
                    a = a[:k+1] + a[k+1:][::-1]
                    return(a)
    return(a)

for i in range((10**6)-1):
    a=reverse(a)

print(a)
print(sum([int(i[1])*10**i[0] for i in enumerate(a[::-1])]))
