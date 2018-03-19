#import
import os
import datetime

#variableDeclaration
timeNow = datetime.date.today()

def begin():
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
    print "      9             KL Sentral         2.10   "
    print "      10           Pasar  Seni         2.10   "
    print "      11          Masjid  Jamek        2.30   "
    print "      12           Dang Wangi          2.30   "
    print "      13          Kampung Baru         2.30   "
    print "      14              KLCC             2.40   "
    print "      15           Ampang Park         2.40   "
    print "      16           Setiawangsa         2.50   "
    print "      17          Terminal Putra       2.50   "

    station = raw_input("\nStation ID : ")

    if ( station == "1" ):
        price = 0.70
        stationName = "Taman Bahagia"
    elif ( station == "2" ):
        price = 1.00
        stationName = "Taman Paramount"
    elif ( station == "3" ):
        price = 1.30
        stationName = "Asia Jaya"
    elif ( station == "4" ):
        price = 1.30
        stationName = "Taman Jaya"
    elif ( station == "5" ):
        price = 1.30
        stationName = "Universiti"
    elif ( station == "6" ):
        price = 1.40
        stationName = "Kerinchi"
    elif ( station == "7" ):
        price = 1.40
        stationName = "Abdullah Hukum"
    elif ( station == "8" ):
        price = 1.40
        stationName = "Bangsar"
    elif ( station == "9" ):
        price = 2.10
        stationName = "KL Sentral"
    elif ( station == "10" ):
        price = 2.10
        stationName = "Pasar Seni"
    elif ( station == "11" ):
        price = 2.30
        stationName = "Masjid Jamek"
    elif ( station == "12" ):
        price = 2.30
        stationName = "Dang Wangi"
    elif ( station == "13" ):
        price = 2.30
        stationName = "Kampung Baru"
    elif ( station == "14" ):
        price = 2.40
        stationName = "KLCC"
    elif ( station == "15" ):
        price = 2.40
        stationName = "Ampang Park"
    elif ( station == "16" ):
        price = 2.50
        stationName = "Setiawangsa"
    elif ( station == "17" ):
        price = 2.50
        stationName = "Terminal Putra"
    else :
        print "\nThe station ID is not recognize. Please try again"
        raw_input("Press Enter to continue.")
        os.system('cls')
        begin()

    #check how much ticket user want to buy
    print "\nPlease type in how many ticket you want to buy."
    amount = input("\nAmount : ")

    #calculate the total amount of money that user need to pay
    total_price = round(price * amount , 3)

    #Paying process
    while ( total_price > 0 ):
        print "\nThe total amount that you need to pay is RM" + str(total_price) + "\n"
        money_pay = input("The money that user insert : RM")
        total_price = round(total_price - money_pay , 3)
        if ( total_price < 0 ):
            balanceTrue(total_price,timeNow,stationName)
        elif ( total_price == 0 ):
            balanceFalse(total_price,timeNow,stationName)

#After paying
def balanceTrue(total_price,timeNow,stationName):
    print "\nThe balance : RM" + str(abs(total_price))
    print "Please take the balance in the dispenser below."
    print "Please take the ticket.\n"
    ticket(timeNow,stationName)
    print "\nThanks for buying ticket with us."
    raw_input("\nPress Enter to continue")
    os.system('cls')
    begin()

def balanceFalse(total_price,timeNow,stationName):
    print "\nPlease take the ticket\n"
    ticket(timeNow,stationName)
    print "\nThanks for buying ticket with us."
    raw_input("\nPress Enter to continue")
    os.system('cls')
    begin()

#Receipt
def ticket(timeNow,stationName):
    print "This is the ticket content."
    print "========================================================================"
    print "Machine No. : 0001                          Date Purchase : " + str(timeNow)
    print ""
    print " ---------------------              ---------------------------"
    print "         From                                    To            "
    print " ---------------------              ---------------------------"
    print "      Kelana Jaya                          " + stationName
    print ""
    print " Thanks for riding with us.                From : LRT Kelana Jaya Staff "
    print "========================================================================"

begin()
