import sys
import os
import random

#Setting Up
read_stone = open("resource\stone.txt","r")
read_wood = open("resource\wood.txt","r")
read_cobblestone = open("resource\cobblestone.txt","r")
read_stick = open("resource\stick.txt","r")
read_log = open("resource\log.txt","r")
read_stoneBrick = open("resource\stoneBrick.txt","r")
read_stonePickaxe = open("resource\stonePickaxe.txt","r")
stone = read_stone.read()
wood = read_wood.read()
cobblestone = read_cobblestone.read()
stick = read_stick.read()
log = read_log.read()
stone_brick = read_stoneBrick.read()
stonePickaxe = read_stonePickaxe.read()

#Variable Declaration
resource = {}
resource["1"] = ["Stone",int(stone),"Most basic material / resource in this game. Mostly used resource."]
resource["2"] = ["Wood",int(wood),"Most basic material / resource in this game. Mostly used resource."]
resource["3"] = ["Cobblestone",int(cobblestone),"Cobblestone sound weak but this item basically used for most of the complex machine or mechanism."]
resource["4"] = ["Stick",int(stick),"Stick is used for many of the tool in this game."]
resource["5"] = ["Log",int(log),"Log is used for more high advance tool."]
resource["6"] = ["Stone Brick",int(stone_brick),"Stone Brick is the advance version of cobblestone but it have only few purpose."]
resource["7"] = ["Stone Pickaxe",stonePickaxe,"Stone Pickaxe allow user to start mining ore such as iron ore and gold ore."]
#[0]:Name of item , [1]:Amount of item required , [2]:Item Description

#Close File
read_stone.close()
read_wood.close()
read_cobblestone.close()
read_stick.close()
read_log.close()
read_stoneBrick.close()
read_stonePickaxe.close()

#Function Declaration
def intro():
    print "Welcome to Crafting Simulator."
    print "This simulator is totally working if you follow the instruction correctly."
    print "Bear in mind that if you force quit this simulator, your progress will removed."

def mine():
    global resource
    if resource["7"][1] == "True" :
        randomizer1 = random.randint(1,3)
        randomizer2 = random.randint(1,5)
        prob = random.random()
        if prob > 0.3:
            print "\nYou gather" , randomizer1 , "iron ore."
        else :
            print "\nYou gather" , randomizer1 , "gold ore."
        print "\nYou gather" , randomizer2 ,  "stone."
    else :
        randomizer = random.randint(1,3)
        print "\nYou gather" , randomizer ,  "stone."
        resource["1"][1] += randomizer

def chop():
    global resource
    randomizer = random.randint(1,3)
    print "\nYou gather" , randomizer ,  "wood."
    resource["2"][1] += randomizer

def station1():
    global resource
    os.system("cls")
    print "Welcome to Crafting Station."
    print "Because it's only newly open, we don't have many thing to offer."
    print "Have a look."
    print "Wood :" , resource["2"][1]
    print "Stone :" , resource["1"][1]
    print "Stick :" , resource["4"][1]
    print "Log :" , resource["5"][1]
    print "Cobblestone :" , resource["3"][1]
    print "Stone Brick :" , resource["6"][1]
    print "Stone Pickaxe :" , resource["7"][1]
    print "\n============================================"
    print " ID      Item        Amount   Requirement"
    print "============================================"
    print " 5       Log           1          4 Wood"
    print " 4      Stick          2          1 Wood"
    print " 7      Stone          1       3 Cobblestone"
    print "       Pickaxe                    2 Stick"
    print " 3   Cobblestone       1          4 Stone"
    print " 6   Stone Brick       1       4 Cobblestone"
    print "============================================\n"

#Starting
intro()
print "\nWhat would you like to do."
print "Wood :" , resource["2"][1]
print "Stone :" , resource["1"][1]
print "1.Mine , 2.Gather Wood , 3.Quit , 10.Crafting Station"
operation = raw_input("\nOperation : ")

while operation != "3":
    if operation == "1":
        mine()
    elif operation == "2":
        chop()
    elif operation == "10":
        station1()
        print "Action : 1.Trade , 2.Item Information , 3.Quit Crafting Station\n"
        action = raw_input("Action : ")
        while action != "3":
            if action == "1":
                print "\nWhich item you need to trade? Type in its ID."
                tradeID = raw_input("ID : ")
                if tradeID == "3":
                    print "\nHow many",resource[tradeID][0],"you want to trade?"
                    amount = raw_input("Amount of item : ")
                    amount = int(amount)
                    totalResource = 4 * amount
                    if resource["1"][1] >= totalResource:
                        resource["1"][1] -= totalResource
                        resource[tradeID][1] += amount
                        print "You successfully trade in" , amount , resource[tradeID][0] , "."
                    else :
                        print "You have no enough stone."
                elif tradeID == "4":
                    print "\nHow many",resource[tradeID][0],"you want to trade?"
                    amount = raw_input("Amount of item : ")
                    amount = int(amount)
                    totalResource = 1 * amount/2
                    if resource["2"][1] >= totalResource:
                        resource["2"][1] -= totalResource
                        resource[tradeID][1] += amount
                        print "You successfully trade in" , amount , resource[tradeID][0] , "."
                    else :
                        print "You have no enough wood."
                elif tradeID == "5":
                    print "\nHow many",resource[tradeID][0],"you want to trade?"
                    amount = raw_input("Amount of item : ")
                    try :
                        amount = int(amount)
                    except ValueError:
                        print "Invalid integer."
                    totalResource = 4 * amount
                    if resource["2"][1] >= totalResource:
                        resource["2"][1] -= totalResource
                        resource[tradeID][1] += amount
                        print "You successfully trade in" , amount , resource[tradeID][0] , "."
                    else :
                        print "You have no enough wood."
                elif tradeID == "6":
                    print "\nHow many",resource[tradeID][0],"you want to trade?"
                    amount = raw_input("Amount of item : ")
                    try :
                        amount = int(amount)
                    except ValueError:
                        print "Invalid integer."
                    totalResource = 4 * amount
                    if resource["3"][1] >= totalResource:
                        resource["3"][1] -= totalResource
                        resource[tradeID][1] += amount
                        print "You successfully trade in" , amount , resource[tradeID][0] , "."
                    else :
                        print "You have no enough cobblestone."
                elif tradeID == "7":
                    if resource[tradeID][1] == "False":
                            if resource["3"][1] >= 3 and resource["4"][1] >= 2:
                                resource["3"][1] -= 3
                                resource["4"][1] -= 2
                                resource[tradeID][1] = "True"
                                print "\nYou successfully trade in stone pickaxe."
                            else :
                                if resource["3"][1] >=3 :
                                    print "\nYou have no enough stick."
                                else :
                                    print "\nYou have no enough cobblestone."
                    else :
                        print "\nYou have already own a stone pickaxe."
                else :
                    print "Invalid Input. Try again"
                raw_input("Press Enter to Continue.")
            
            elif action == "2":
                print "Which item you need to check? Type in their ID."
                checkID = raw_input("ID :")
                if checkID in resource :
                    print "Item ID :" , checkID
                    print "Item Name :" , resource[checkID][0]
                    print "Item Description :" , resource[checkID][2]
                else :
                    "Invalid input. Try again."
                raw_input("Press Enter to Continue.")

            else :
                print "Invalid Input. Try again."

            station1()
            print "Action : 1.Trade , 2.Item Information , 3.Quit Crafting Station\n"
            action = raw_input("Action : ")
        
        else :
            print "Thanks for coming. See you again."
    else :
        print "Invalid Input. Try again."
    
    raw_input("Press Enter to Continue.")
    os.system("cls")
    print "What would you like to do."
    print "Wood :" , resource["2"][1]
    print "Stone :" , resource["1"][1]
    print "1.Mine , 2.Gather Wood , 3.Quit , 10.Crafting Station"
    operation = raw_input("\nOperation : ")

else :
    print "Thanks for playing."
    print "Your resource is saved and you can continue play with your current balance next time you open the game."
    #Open text file to replace data
    write_stone = open("resource\stone.txt","w")
    write_wood = open("resource\wood.txt","w")
    write_cobblestone = open("resource\cobblestone.txt","w")
    write_stick = open("resource\stick.txt","w")
    write_log = open("resource\log.txt","w")
    write_stoneBrick = open("resource\stoneBrick.txt","w")
    write_stonePickaxe = open("resource\stonePickaxe.txt","w")

    #Changing data
    write_stone.write(str(resource["1"][1]))
    write_wood.write(str(resource["2"][1]))
    write_cobblestone.write(str(resource["3"][1]))
    write_stick.write(str(resource["4"][1]))
    write_log.write(str(resource["5"][1]))
    write_stoneBrick.write(str(resource["6"][1]))
    write_stonePickaxe.write(resource["7"][1])

    #Close the files
    write_stone.close()
    write_wood.close()
    write_cobblestone.close()
    write_stick.close()
    write_log.close()
    write_stoneBrick.close()
    write_stonePickaxe.close()

    sys.exit()