import random as r

player = {
    "maxHP" : 500,
    "HP" : 0,
    "atk" : 40,
    "def" : 20
}

enemy = {
    "maxHP" : 300,
    "HP" : 0,
    "atk" : 60,
    "def" : 10
}

def critPlayer(critRate):
    global dd
    m = r.random()
    if m > 0.7:
        dd *= 1 + critRate
        dd = int(dd)

def critEnemy(critRate):
    global dt
    m = r.random()
    if m > 0.7:
        dt *= 1 + critRate
        dt = int(dt)

player["HP"] = player["maxHP"]
enemy["HP"] = enemy["maxHP"]
critRate = round(r.uniform(0,0.4),2)

while player["HP"] > 0 and enemy["HP"] > 0 :
    print "Player HP :" , player["HP"]
    print "Enemy HP  :" , enemy["HP"]
    #De-bug session
    #print critRate
    #print "In order to Run, enemy HP should less than" , enemy["maxHP"] * 0.2 , "."
    print "\n1. Attack\n2. Run"
    order = raw_input("\nOrder : ")
    if order == "1":
        dd = player["atk"] - enemy["def"]
        critPlayer(critRate)
        enemy["HP"] -= dd
        print "\nPlayer dealt" , dd , "to enemy."
        if ( enemy["HP"] <= 0 ):
            print "Enemy slain."
            break
        dt = enemy["atk"] - player["def"]
        critEnemy(critRate)
        player["HP"] -= dt
        print "Enemy dealt" , dt , "to player.\n"
        if ( player["HP"] <= 0 ):
            print "Player died. Game Over."
            break
    elif order == "2":
        if enemy["HP"] < enemy["maxHP"] * 0.2 :
            print "\nPlayer manage to escape from enemy's attack.\n"
            break
        else :
            print "\nPlayer fail to escape from enemy's attack.\n"
    else :
        print "\nWrong comand. Please re-type.\n"

raw_input("\nThanks for playing.")
