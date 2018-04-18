import math

c1 = (0,0)
c2 = (5,2)
c3 = (4,7)
c4 = (5,0)
c5 = (0,8)

C1 = [ c2 , c3 , c4 , c5 ]
C2 = [ c1 ]
length = len(C1)
m = 0
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

while m < length:
    d = []
    for n in C1:
       distanceAppend(C2[m],n)
    else:
        print d
        minimum_distance = min(d)
        print minimum_distance
        for n in C1:
            if distanceCheck(C2[m],n) == minimum_distance:
                C2.append(n)
                C1.remove(n)
        print C1
        print C2
        print "=============================="
        m += 1
else:
    x = 0
    while x < len(C2) - 1:
        distanceCalculate(C2[x],C2[x+1])
        x += 1

    print total_distance
        
