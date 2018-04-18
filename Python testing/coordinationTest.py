import math

C1 = []
C2 = [ (0,0) ]
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

print "Welcome to the system."
print "The first coordinate is set as (0,0) since it start from there."
console = raw_input("If you want to stop adding coordinate, type in 'S'.\nIf not press Enter.")

while console != "S":
    x_input = input("Please enter the x coordinate.")
    y_input = input("Please enter the y coordinate.")
    coordinate = (x_input,y_input)
    C1.append(coordinate)
    console = raw_input("If you want to stop adding coordinate, type in 'S'.\nIf not press Enter.")

else :
    print C1
    length = len(C1)
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
