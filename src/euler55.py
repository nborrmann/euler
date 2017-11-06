

def reverse(num):
    return(int(str(num)[::-1]))


c=0
for n in range(0,10000):
    lych=True
    n_rev=reverse(n)
    n+=n_rev

    for i in range(1,53):
        n_rev=reverse(n)
        if(n == n_rev):
            lych=False
            break
        n+=n_rev

    if(lych):
        c+=1


print(c)




