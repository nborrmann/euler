from datetime import datetime


startTime = datetime.now()
for i in range(10**7):
    x = int(i/7)
print(datetime.now()-startTime)

startTime = datetime.now()
for i in range(10**7):
    x = i//7
print(datetime.now()-startTime)
