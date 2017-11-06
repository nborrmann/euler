import math

n=1000000000

r_squ = n**2//32
r_bound = int(math.sqrt(r_squ))+1
int_points=0

#right half of circle
y=r_bound
for x in range(1,r_bound):
    while (y**2 >= r_squ - x**2):
        y-=1
    int_points += 2*y+1

int_points*=2 #adds left half of circle
int_points+=(2*int(math.sqrt(r_squ))+1) #adds mid of circle

int_points -= (n//4)-1 #diagonal
int_points += n*n      #bottom rectangle
int_points += n*n//2   #top rectangle

print(int_points)