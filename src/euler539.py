import math
import  tqdm

solutions = []

# 0.75*i*i - 0.5*i - 0.25
# 0.75 ( i**2 - 2/3*i - 1/3)
# 0.75 (i**2 - 2/3*i + 1/9 - 4/9)
# 0.75 (i-1/3)**2 - 1/3

##for i in range(3, 100, 2):
##    k_square =  0.75*i*i - 0.5*i - 0.25
##    k = math.sqrt(k_square)
##    if round(k)**2 == k_square:
##        print(i, k)
##
##    k_square += i
##    k = math.sqrt(k_square)
##    if round(k)**2 == k_square:
##        print(i, k)
##
##print(solutions)
##
##max_n = 100
##max_k = 0.75*max_n*max_n - 0.5*max_n - 0.25
##
##for k in range(2, int(math.sqrt(max_k))+2):
##    # k_square = k*k
##    # 0.75*x*x - 0.5*x - 0.25 - k*k = 0
##    x1 = 1/3 * ( 1 - 2*math.sqrt(3*k*k +1) )
##    x2 = 1/3 * ( 1 + 2*math.sqrt(3*k*k +1) )
##    print(k, x1, x2, 3*k*k+1)

def is_square(n):
    return round(math.sqrt(n))**2 == n

##total = 10**12
##b = 10**12 / 2 # number of blue disks
##r = total - b
##
### b * (b-1) / (total * (total-1)) = 0.5
### b*b - b / (total**2 -total) = 0.5
##c = 0.5 * (total**2 - total)
### b*b - b - c = 0
### b**2 - b + 1/4 = c - 1/4
### (b - 1/2)**2 = 0.5 * total**2 - 0.5 * total - 1/4
##
##x1 = 1 + math.sqrt(1 + 4*c) / 2
##x1 = 1 + math.sqrt(1 + 2 * (total**2 - total)) / 2
### x2 = 1 - math.sqrt(1 + 4*c) / 2
##
##n = 10**12
##for total in range(1070379110497, 1070379110497+1):
##    x1 = 1 + math.sqrt(1 + 2 * (total**2 - total)) / 2
##    print(x1)
##    print(total, math.sqrt(2 * total**2 - 2 * total + 1))
##    #if is_square(1 + 2 * (total**2 - total)):
##    #    print(total)
##
### k**2 = (total - 1)**2

def is_pandigital(n_str):
    return '1' in n_str and '2' in n_str and '3' in n_str and '4' in n_str and '5' in n_str and '6' in n_str and '7' in n_str and '8' in n_str and '9' in n_str

f0 = 0
f1 = 1

f0_first = 0
f1_first = 1

f0_last = 0
f1_last = 1

i = 2
while 1:
    f1, f0 = f1+f0, f1

    if is_pandigital(str(f1)[:9]) and is_pandigital(str(f1)[-9:]):
        print(i, f1, str(f1)[-11:])
        break
    i+=1


    
    




































    
    
