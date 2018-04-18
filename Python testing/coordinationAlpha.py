import math

c1 = (0,0)
c2 = (5,2)
c3 = (4,7)
c4 = (5,0)
c5 = (0,8)

C1 = [ c2 , c3 , c4 , c5 ]
C2 = [ c1 ]

d = []
total_distance = 0.0


def distanceAppend(x,y):
    cz = ( y[0] - x[0] , y[1] - x[1] ) 
    if cz[0] == 0:
        d.append(cz[1])
    elif cz[1] == 0:
        d.append(cz[0])
    else :
        d.append(round(math.sqrt( ( cz[0] ** 2 ) + ( cz[1] ** 2 ) ),2))

def distanceCheck(x,y):
    cz = ( y[0] - x[0] , y[1] - x[1] ) 
    if cz[0] == 0:
        return cz[1]
    elif cz[1] == 0:
        return cz[0]
    else :
        return round(math.sqrt( ( cz[0] ** 2 ) + ( cz[1] ** 2 ) ),2)

def distanceCalculate(x,y):
    global total_distance
    cz = ( y[0] - x[0] , y[1] - x[1] ) 
    if cz[0] == 0:
        d = cz[1]
    elif cz[1] == 0:
        d = cz[0]
    else :
        d = round(math.sqrt( ( cz[0] ** 2 ) + ( cz[1] ** 2 ) ),2)
    total_distance += d
        
for x in C1:
    distanceAppend(C2[0],x)
else:
    print d
    minimum_distance = min(d)
    print minimum_distance
    for m in C1:
        if distanceCheck(C2[0],m) == minimum_distance:
            C2.append(m)
            C1.remove(m)

print C1
print C2
print "=============================="

d = []

for x in C1:
    distanceAppend(C2[1],x)
else:
    print d
    minimum_distance = min(d)
    print minimum_distance
    for m in C1:
        if distanceCheck(C2[1],m) == minimum_distance:
            C2.append(m)
            C1.remove(m)

print C1
print C2
print "=============================="

d = []

for x in C1:
    distanceAppend(C2[2],x)
else:
    print d
    minimum_distance = min(d)
    print minimum_distance
    for m in C1:
        if distanceCheck(C2[2],m) == minimum_distance:
            C2.append(m)
            C1.remove(m)

print C1
print C2
print "=============================="

d = []

for x in C1:
    distanceAppend(C2[3],x)
else:
    print d
    minimum_distance = min(d)
    print minimum_distance
    for m in C1:
        if distanceCheck(C2[3],m) == minimum_distance:
            C2.append(m)
            C1.remove(m)

print C2
print "=============================="
x = 0
while x < len(C2) - 1:
    distanceCalculate(C2[x],C2[x+1])
    x += 1

print total_distance

#print minimum_distance
#print total_distance

#total_distance = 15.33
#gradient(c1,c4)
#gradient(c4,c2)
#gradient(c2,c3)
#gradient(c3,c5)
#gradient(c5,c1)

#total_distance = 22.4
#gradient(c1,c2)
#gradient(c2,c3)
#gradient(c3,c4)
#gradient(c4,c5)
#gradient(c5,c1)
