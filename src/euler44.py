import math

def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


def number_of_factors_in_factorial(n, f):
    count, f_k = 0, f

    while f_k <= n:
        count += n//f_k
        f_k *= f

    return count


def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


n = 10**12
#n=20
f_of_n = 1
missing_twos = 0
for i in range(1, 10**5):
    while i % 5 == 0:
        i /= 5
        missing_twos += 1

    while missing_twos>0 and i % 2 == 0:
        i //= 2
        missing_twos -= 1

    f_of_n *= pow_mod(i, 10**7, 10**5)
    f_of_n %= 10**5
    #print(int(i), int(pow_mod(i, 1, 10**5)))
    #print(i, pow_mod(i, 10**1, 10**5))

print(missing_twos, f_of_n)

# for i in primes_sieve(n+1):
#     #if i == 5:
#     #    continue
#
#     #f_of_n *= pow_mod(i, number_of_factors_in_factorial(n, i), 10**11)
#     f_of_n *= (i ** number_of_factors_in_factorial(n, i))
#     print(i, number_of_factors_in_factorial(n, i))
#     #f_of_n %= 10**11
#
# print(f_of_n, math.factorial(n))

# twos_in_n = number_of_factors_in_factorial(10**12, 2)
# print(pow_mod(2, twos_in_n, 10*10))
# print(number_of_factors_in_factorial(10**12, 2))
# print(number_of_factors_in_factorial(10**12, 3))
# print(number_of_factors_in_factorial(10**12, 5))
# print(number_of_factors_in_factorial(10**12, 7))
# print(number_of_factors_in_factorial(10**12, 11))
# print(number_of_factors_in_factorial(10**12, 13))
# print(number_of_factors_in_factorial(10**12, 17))

