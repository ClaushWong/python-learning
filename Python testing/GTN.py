import random
minInt = input("Please type in the minimum integer.")
maxInt = input("Please type in the maximum integer.")
guess = False

while guess == False :
    x = random.randint(minInt,maxInt)
    print x
    question = raw_input("\nIs this number greater or lower than your exact number?\nOr is it the exact number you searching for (G/L/E) ")
    if question == "G":
        minInt = x
    elif question == "L":
        maxInt = x
    elif question == "E":
        print "\nI got it. It's" , x , "."
        guess = True
    else :
        print "Error"

    if minInt + 1 == maxInt - 1:
        print "\nI got it. It's" , minInt + 1 , "."
        guess = True

raw_input("Press any key to escape.")
