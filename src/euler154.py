import tqdm

d = {}

def calc_fives_in_fac(n):
    if d.get(n):
        return d.get(n)

    f, fives = 5, 0

    while f < n:
        fives += n // f
        f *= 5

    d[n] = fives
    return fives

count = 0
count_ = 0

n = 2000
n_fixed = 2000//5
fives_in_n = calc_fives_in_fac(n)

for i in tqdm.tqdm(range(n), ncols=100, ascii=True):
    fives_in_i = calc_fives_in_fac(i)
    for j in range(n - i):
        k = n - i - j
        if fives_in_n - fives_in_i - calc_fives_in_fac(j) - calc_fives_in_fac(k) >= 12:
            count += 1

            if n == 0:
                count_ += 1
            if i == 0:
                count_ += 1
            if j == 0:
                count_ += 1

print(count)
#print(count, 2001000/count)

#print(count*25 - count_*5)
