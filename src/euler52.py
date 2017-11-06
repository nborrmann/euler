




for i in range(2,7):
    maxValue = int(10/6*(10**i))

    for j in range(10**i, maxValue):
        multiples = [j*k for k in range(2,6)]
        j_digits=[int(j%(10**k)/(10**(k-1))) for k in range(1,i+2)]

        c=0
        for m in multiples:
            m_digits=[int(m%(10**k)/(10**(k-1))) for k in range(1,i+2)]
            if(len(set(m_digits).intersection(j_digits)) != i+1):
                break
            else:
                c+=1

        if(c==4):
            print(j, i)
            exit()









