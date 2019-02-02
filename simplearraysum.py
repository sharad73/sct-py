#!/usr/bin/python3
#The function adds the given array elements and return sum of array
ar=(1,2,3,4,10,11)
def sumofarray(ar):
	result=0
	n=len(ar)
	print("The length of array is %d"%(n))
	for i in range(n):
		result=result+ar[i]
	print ("The sum of array element is %d" %(result))

		
sumofarray(ar)	