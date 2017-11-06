#works but too slow

def is_reversible(n):
    n += int(str(n)[::-1])

    while n:
        if (n%2 == 0):
            return False
        n//=10
    return True

print(sum(1 if (n%10 != 0 and is_reversible(n)) else 0 for n in range(10**9)))
