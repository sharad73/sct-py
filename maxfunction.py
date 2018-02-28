#!/usr/bin/python2.7

import sys

def getMax( set ):
   max = set[0]
   i = 1   
   while( i < 5 ):
      if( max <  set[i] ):
         max = set[i]
         print max
      i = i + 1
   return max


set1 = [10, 20, 30, 40, 50]
set2 = [101, 201, 301, 401, 501]



# Process first set of numbers available in set1[]
max = getMax(set1)
print "Max in first set = ", max
    
# Now process second set of numbers available in set2[]
max = getMax(set2)
print "Max in second set = ", max

#set1 = [10, 20, 30, 40, 50]
#print max(set1)

list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
list1 = list(list1)
print list1
print "Max value element : ", max(list1)
print "Max value element : ", max(list2)
