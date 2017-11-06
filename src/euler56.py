def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, int(n / 10)
   return(r)

def sum_digits2(n):
    return(sum(int(digit) for digit in str(n)))

maxValue = 0
for i in range(100):
    for j in range(100):
        s=sum_digits2(i**j)
        if(s>maxValue):
            maxValue=s

print(maxValue)
print("hallo")

