
def cycle_len(n):
    remainder, l = 1, []
    while (not remainder in l) and (not remainder == 0):
        l.append(remainder)
        remainder = remainder*10%n

    return(len(l[l.index(remainder):]) if (remainder != 0) else 0)

print(max([(cycle_len(i),i) for i in range(1,1000)]))
