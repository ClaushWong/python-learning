import random as r

first_attack = 250
crit_ratio = 0.05
turn = 1
enemyHP = 2000

print crit_ratio
print "=========="

while turn < 4 :
    final_attack = first_attack + first_attack * r.uniform(0,crit_ratio)
    enemyHP -= round(final_attack,2)
    print round(final_attack,0)
    print enemyHP
    turn += 1
