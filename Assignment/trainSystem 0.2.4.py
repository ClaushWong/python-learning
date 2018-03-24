#import
import os
import datetime

#variableDeclaration
timeNow = datetime.date.today()
stationList = ["Taman Bahagia", "Taman Paramount", "Asia Jaya", "Taman Jaya", "Universiti", "Kerinchi" , "Abdullah Hukum" , "Bangsar", "KL Sentral", "Pasar Seni", "Masjid Jamek", "Dang Wangi","Kampung Baru","KLCC","Ampang Park","Setiawangsa","Terminal Putra"]
stationPriceList = [0.70,1.00,1.30,1.30,1.30,1.40,1.40,1.40,2.10,2.10,2.30,2.30,2.30,2.40,2.40,2.50,2.50]
note_syilling_accepted = [ 1 , 2 , 5 , 10 , 0.1 , 0.2 , 0.5 ]
ticket_available = [ 20 , 20 , 15 , 14 , 13 , 10 , 5 , 10 , 12 , 17 , 50 , 20 , 13 , 15 , 16 , 23 , 11 ]

#Starting
def list1():
    print "====================================================="
    print " Welcome to the Kelana Jaya LRT Ticket Buying System"
    print "====================================================="

    #check which station user want to go
    print "Which station you need to go from Kelana Jaya Station?"
    print "\n============   ================== ============ =========="
    print " Station ID       Station Name      Price(RM)    Amount  "
    print "============   ================== ============ =========="
    print "      1           Taman Bahagia        0.70        " + str(ticket_available[0])
    print "      2          Taman Paramount       1.00        " + str(ticket_available[1])
    print "      3            Asia  Jaya          1.30        " + str(ticket_available[2])
    print "      4           Taman  Jaya          1.30        " + str(ticket_available[3])
    print "      5             Universiti         1.30        " + str(ticket_available[4])
    print "      6              Kerinchi          1.40        " + str(ticket_available[5])
    print "      7           Abdullah Hukum       1.40        " + str(ticket_available[6])
    print "      8              Bangsar           1.40        " + str(ticket_available[7])
    print "\n                                             Page : 1 / 2"
    print "\nInsert '20' to page 2."

def list2():
    print "====================================================="
    print " Welcome to the Kelana Jaya LRT Ticket Buying System"
    print "====================================================="

    #check which station user want to go
    print "Which station you need to go from Kelana Jaya Station?"
    print "\n============   ================== ============ =========="
    print " Station ID       Station Name      Price(RM)    Amount  "
    print "============   ================== ============ =========="
    print "      9             KL Sentral         2.10        " + str(ticket_available[8])
    print "      10           Pasar  Seni         2.10        " + str(ticket_available[9])
    print "      11          Masjid  Jamek        2.30        " + str(ticket_available[10])
    print "      12           Dang Wangi          2.30        " + str(ticket_available[11])
    print "      13          Kampung Baru         2.30        " + str(ticket_available[12])
    print "      14              KLCC             2.40        " + str(ticket_available[13])
    print "      15           Ampang Park         2.40        " + str(ticket_available[14])
    print "      16           Setiawangsa         2.50        " + str(ticket_available[15])
    print "      17          Terminal Putra       2.50        " + str(ticket_available[16])
    print "\n                                             Page : 2 / 2"
    print "\nInsert '19' to page 1."

def begin():
    station = raw_input("\nStation ID : ")
    try :
        station = int(station)
    
    except ValueError:
        print "The station you typed is not recognized. Please try again."
        raw_input("Press Enter to continue.")
        os.system('cls')
        list1()
        begin()

    else :
        if ( ticket_available[station-1] != 0 ):
            if ( station > 0 and station < 18 ):
                print "\nProcessing... Please Wait"
                #check how much ticket user want to buy
                amount_want_to_buy(station)   
        
            elif ( station == 20 ):
                os.system('cls')
                list2()
                begin()
            elif( station == 19 ):
                os.system('cls')
                list1()
                begin()
            else :
                print "\nThe station ID is not recognize. Please try again"
                raw_input("Press Enter to continue.")
                os.system('cls')
                list1()
                begin()
        else  :
           print "\nThis station's ticket is run out. We're sorry."
           raw_input("Press Enter to escape.")
           os.system('cls')
           list1()
           begin()

#After paying
def balanceTrue(total_price,timeNow,stationName,amount):
    print "\nThe balance : RM" + str(abs(total_price))
    print "Please take the balance in the dispenser below."
    print "Please take the ticket.\n"
    ticket(timeNow,stationName,amount)
    print "\nThanks for buying ticket with us."
    raw_input("\nPress Enter to continue")
    os.system('cls')
    list1()
    begin()

def balanceFalse(total_price,timeNow,stationName,amount):
    print "\nPlease take the ticket\n"
    ticket(timeNow,stationName,amount)
    print "\nThanks for buying ticket with us."
    raw_input("\nPress Enter to continue")
    os.system('cls')
    list1()
    begin()

#Receipt
def ticket(timeNow,stationName,amount):
    print "This is the ticket content."
    print "========================================================================"
    print "Machine No. : 0001                          Date Purchase : " + str(timeNow)
    print ""
    print "Number of ticket buyed : " + str(amount)
    print ""
    print " ---------------------              ---------------------------"
    print "         From                                    To            "
    print " ---------------------              ---------------------------"
    print "      Kelana Jaya                        " + stationName
    print ""
    print " Thanks for riding with us.                From : LRT Kelana Jaya Staff "
    print "========================================================================"

def amount_want_to_buy(station):
    print "\n========================================================"
    print "\nPlease type in how many ticket you want to buy."
    print "Available tickets : " + str(ticket_available[station-1])
    amount = input("\nAmount : ")
    try :
        amount = int(amount)
    except ValueError:
        print "Please give a valid integer value. Try again."
    else :
        if ( amount > ticket_available[station-1] ):
            raw_input("The amount you want is more than the ticket we have. Please reconsider.")
            os.system('cls')
            amount_want_to_buy(station)
        else :
            ticket_available[station-1] -= amount
            #calculate the total amount of money that user need to pay
            total_price = round(stationPriceList[station-1] * amount , 2)
            #Paying process
            os.system('cls')
            paying_process(amount,station,total_price)
            
def paying_process(amount,station,total_price):
    while ( total_price > 0 ):
        print "Station name : " + stationList[station-1]
        print "Number of ticket : " + str(amount) 
        print "The total amount that you need to pay is RM" + str(total_price) + "\n"
        money_pay = input("The money that user insert : RM")
               
        if money_pay in note_syilling_accepted:
            total_price = round(total_price - money_pay , 3)
            if ( total_price < 0 ):
                os.system('cls')
                balanceTrue(total_price,timeNow,stationList[station-1],amount)
            elif ( total_price == 0 ):
                os.system('cls')
                balanceFalse(total_price,timeNow,stationList[station-1],amount)
            os.system('cls')
        else :
            print "The syilling or note is not valid. Try again."
            raw_input("Press Enter to escape.")
            os.system('cls')

list1()
begin()
