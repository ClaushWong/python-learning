def add(a,b):
    c = a + b
    print "\nThe addition of " + str(a) + " and " + str(b) + " is " + str(c) + ".\n"

def sub(a,b):
    c = a - b
    print "\nThe subtraction of " + str(a) + " and " + str(b) + " is " + str(c) + ".\n"

def mult(a,b):
    c = a * b
    print "\nThe multiplication of " + str(a) + " and " + str(b) + " is " + str(c) + ".\n"

def div(a,b):
    c = a / b
    print "\nThe division of " + str(a) + " and " + str(b) + " is " + str(c) + ".\n"

def power(a,b):
    c = a ** b
    print "\n" + str(a) + " power of " + str(b) + " is equal to " + str(c) + ".\n"

def start():
    oper = input("Please ennter the operation you want to use based on the list below.\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponential / Power Of\n20. Exit\n")

    if oper == 1 :
        num1 = input("Please enter the first number.\n")
        num2 = input("Please enter the second number.\n")
        add(num1,num2)
        start()

    elif oper == 2 :
        num1 = input("Please enter the first number.\n")
        num2 = input("Please enter the second number.\n")
        sub(num1,num2)
        start()

    elif oper == 3 :
        num1 = input("Please enter the first number.\n")
        num2 = input("Please enter the second number.\n")
        mult(num1,num2)
        start()

    elif oper == 4 :
        num1 = input("Please enter the first number.\n(Integer : 1 , Float : 1.0)\n")
        num2 = input("Please enter the second number.\n(Integer : 1 , Float : 1.0)\n")
        div(num1,num2)
        start()

    elif oper == 5 :
        num1 = input("Please enter the base value.\n")
        num2 = input("Please enter the exponent value / pawer value.\n")
        power(num1,num2)
        start()

    elif oper == 20 :
        print "\nThanks for using.\n"

    else :
        print "\nError input, try again.\n"
        start()

start()
