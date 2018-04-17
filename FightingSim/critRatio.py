import random as r
critRate = 0.5
counter = 0
csp = 0.9
cse = 0.9
ncsp = csp
ncse = cse

dd = 500
dt = 350

def critPlayer(critRate):
    global dd
    global csp
    global ncsp
    print "======="
    print ncsp
    m = r.random()
    if m > ncsp:
        dd *= 1 + critRate
        dd = int(dd)
        ncsp -= 0.1
    else :
        ncsp = csp
    
def critEnemy(critRate):
    global dt
    m = r.random()
    if m > cse:
        dt *= 1 + critRate
        dt = int(dt)

while counter < 100:
    critPlayer(critRate)
    counter += 1
