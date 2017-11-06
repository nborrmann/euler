from datetime import datetime
startTime = datetime.now()
##################################

f=open("euler81.txt","r")
matrix = [[int(n) for n in line.split(',')] for line in f]

for n in range(1,80*2):
    for j in range(n+1):
        if (j>=80 or n-j>=80):
            continue
        if (j==0):
            matrix[j][n-j] += matrix[j][n-j-1]
        elif (n-j==0):
            matrix[j][n-j] += matrix[j-1][n-j]
        else:
            matrix[j][n-j] += min(matrix[j-1][n-j],matrix[j][n-j-1])

print(matrix[79][79])

###################################
print(datetime.now()-startTime)
