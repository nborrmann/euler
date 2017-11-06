from datetime import datetime
startTime = datetime.now()
##################################

f=open("euler81.txt","r")
matrix = [[int(n) for n in line.split(',')] for line in f]

x0, y0 = 0,1

n=1
for i in range(-n,n+1):
    x = n-abs(i) + x0
    y = i + y0
    print(x,y)

    if (x>=80 or y>=80 or x<0 or y < 0):
        continue
    if (x == 0 and i <= 0):
        matrix[y][x] += matrix[y+1][x]
    if (x == 0 and i >= 0):
        matrix[y][x] += matrix[y-1][x]


for i in range(4):
    print(matrix[i][0:4])


#for n in range(1,80*2):
    #for j in range(n+1):
        #if (j>=80 or n-j>=80):
        #    continue
        #if (j==0):
        #    matrix[j][n-j] += matrix[j][n-j-1]
        #elif (n-j==0):
        #    matrix[j][n-j] += matrix[j-1][n-j]
        #else:
        #    matrix[j][n-j] += min(matrix[j-1][n-j],matrix[j][n-j-1])

#print(matrix[79][79])

###################################
#print(datetime.now()-startTime)
