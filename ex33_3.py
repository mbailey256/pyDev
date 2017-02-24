
from sys import argv

script,var1,var4 = argv
#var1 = int(var1)


def list(var2,var3):

    i = 0
    numbers = []


    for i in range(int(var2)):
        print "At the top i is %d" % i
        numbers.append(i)

#        i = i + int(var3)  # This is no longer needed within the for loop
        print "Numbers now: " , numbers
        print "At the bottom i is %d" % i



    print "The numbers: "

    for num in numbers:
        print num

list(var1,var4)
