from datetime import datetime
startTime = datetime.now()
##################################

f=open("euler67.txt","r")
lines = [[int(n) for n in line.split(' ')] for line in f]

for i in range(len(lines)-2,-1,-1):
    lines[i] = [lines[i][j] + max(lines[i+1][j], lines[i+1][j+1]) for j in range(0,i+1)]

print(lines[0][0])

###################################
print(datetime.now()-startTime)
