n = 28433

for i in range(7830457):
    n= (n*2)%10**10

print(n+1)

#(28433*pow(2,7830457,10000000000)+1)%10000000000