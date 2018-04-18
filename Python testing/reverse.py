#x = raw_input("Please enter your string.\n")
#y = []

#count = len(x)

#while count != 0:
    #y.append(x[count-1])
    #count -= 1

#z = ''.join(y)
#raw_input(z)

def reverse(x):
    y = []
    count = len(x)
    while count != 0:
        y.append(x[count-1])
        count -= 1

    z = ''.join(y)
    print z
    print len(z)
    
