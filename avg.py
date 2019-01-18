##!/usr/lib/python

def avg(list):
    #list = [3,7,5,2,1,6]
    print ("list is: %s " %list)
    i = 0
    sum = 0
    while i < len(list):
        sum = sum + list[i]
        print ("sum %d: " %sum)
        i +=  1
    #avg = sum/float(len(list))
    avg = sum/len(list)
    #print "Avg of the list is %.2f " %avg
    print ("Avg of the list is %d " %avg)
    return avg

avg([3,7,5,2,1,6])
