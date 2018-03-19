#import
import os
import datetime

#variableDeclaration
timeNow = datetime.date.today()
stationList = ["Taman Bahagia", "Taman Paramount", "Asia Jaya", "Taman Jaya", "Universiti", "Kerinchi" , "Abdullah Hukum" , "Bangsar", "KL Sentral", "Pasar Seni", "Masjid Jamek", "Dang Wangi","Kampung Baru","KLCC","Ampang Park","Setiawangsa","Terminal Putra"]
stationPriceList = [0.70,1.00,1.30,1.30,1.30,1.40,1.40,1.40,2.10,2.10,2.30,2.30,2.30,2.40,2.40,2.50,2.50]

#Starting
def list1():
    print "====================================================="
    print " Welcome to the Kelana Jaya LRT Ticket Buying System"
    print "====================================================="

    #check which station user want to go
    print "Which station you need to go from Kelana Jaya Station?"
    print "\n============   ================== ============"
    print " Station ID       Station Name      Price(RM) "
    print "============   ================== ============"
    print "      1           Taman Bahagia        0.70   "
    print "      2          Taman Paramount       1.00   "
    print "      3            Asia  Jaya          1.30   "
    print "      4           Taman  Jaya          1.30   "
    print "      5             Universiti         1.30   "
    print "      6              Kerinchi          1.40   "
    print "      7           Abdullah Hukum       1.40   "
    print "      8              Bangsar           1.40   "
    print "                                  Page : 1 / 2"
    print "\nInsert '20' to page 2."

def list2():
    print "====================================================="
    print " Welcome to the Kelana Jaya LRT Ticket Buying System"
    print "====================================================="

    #check which station user want to go
    print "Which station you need to go from Kelana Jaya Station?"
    print "\n============   ================== ============"
    print " Station ID       Station Name      Price(RM) "
    print "============   ================== ============"
    print "      9             KL Sentral         2.10   "
    print "      10           Pasar  Seni         2.10   "
    print "      11          Masjid  Jamek        2.30   "
    print "      12           Dang Wangi          2.30   "
    print "      13          Kampung Baru         2.30   "
    print "      14              KLCC             2.40   "
    print "      15           Ampang Park         2.40   "
    print "      16           Setiawangsa         2.50   "
    print "      17          Terminal Putra       2.50   "
    print "                                  Page : 2 / 2"
    print "\nInsert '19' to page 1."

def begin():
    station = raw_input("\nStation ID : ")
    try :
        station = int(station)
        if ( station > 0 and station < 18):
            print "\nProcessing... Please Wait"
            #check how much ticket user want to buy
            print "\n========================================================"
            print "\nPlease type in how many ticket you want to buy."
            amount = input("\nAmount : ")
            try :
                amount = int(amount)
            except ValueError:
                print "Please give a valid integer value. Try again."
            
            #calculate the total amount of money that user need to pay
            total_price = round(stationPriceList[station-1] * amount , 2)

            #Paying process
            os.system('cls')
            while ( total_price > 0 ):
                print "Station name : " + stationList[station-1]
                print "Number of ticket : " + str(amount) 
                print "The total amount that you need to pay is RM" + str(total_price) + "\n"
                money_pay = input("The money that user insert : RM")
                total_price = round(total_price - money_pay , 3)
                if ( total_price < 0 ):
                    os.system('cls')
                    balanceTrue(total_price,timeNow,stationList[station-1],amount)
                elif ( total_price == 0 ):
                    os.system('cls')
                    balanceFalse(total_price,timeNow,stationList[station-1],amount)
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
    except ValueError:
        print "The station you typed is not recognized. Please try again."
        raw_input("Press Enter to continue.")
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

list1()
begin()
