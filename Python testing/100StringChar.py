import random
import reverse as rev

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','#']

z = []

count = 0

while count != 100:
    n = random.randint(0,53)
    z.append(a[n])
    count += 1

m = ''.join(z)

print m
print len(m)

print ""
print ""

rev.reverse(m)
