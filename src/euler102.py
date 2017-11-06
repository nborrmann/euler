f = open("triangles.txt")

P = [0,0]
count = 0
for line in f.readlines():
    coords = [int(x) for x in line.strip().split(",")]
    v00 = coords[4]-coords[0]
    v01 = coords[5]-coords[1]
    v10 = coords[2]-coords[0]
    v11 = coords[3]-coords[1]
    v20 = P[0]-coords[0]
    v21 = P[1]-coords[1]
    u = ((v11*v20)-(v10*v21)) / ((v00*v11) - (v01*v10))
    v = ((v00*v21)-(v01*v20)) / ((v00*v11) - (v01*v10))
    if (0<u<1 and 0<v<1):
        count+=1
    #print(count)

print(count)
