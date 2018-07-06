import sys

def printFunStuff():
    var1 = raw_input("Please enter a number: ")
    var2 = raw_input("Please enter another number: ")
    #sum = (var1 * var2)

    #print var1, "*", var2, "=", sum
    if( var1.isdigit()):
        sum = int(var1) * int(var2)
        print var1, "*", var2, "=", sum
    else:
        print "You need to enter a number!"

printFunStuff()
