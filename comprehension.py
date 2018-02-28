#!/usr/bin
#Given list
nums = [1,2,3,4,5,6,7,8,9,10] 
#I want square of the number
#Normal way
##my_list = []
##for n in nums:
##    my_list.append(n*n)
##print my_list

#List Comprehension way. I want square of the each number in the list   
#my_list = [n*n for n in nums]
#print my_list

#I want n for each n if n is even
##my_list = [n for n in nums if n % 2 == 0]
##print my_list

#I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
##my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
##print my_list

# Take two digit integer say 19 and calculate the square of each digit.
#Add the square numbers and continue, until there sum become 1
n = str(19)
print "The number is {}".format(n) 
while n != 1:
    my_list = list(n)
    print "Number converted in to list {}".format(my_list)
    x = int(my_list[0])
    y = int(my_list[1])
    #print y
    n = str(int(x**2 + y**2))
    print "The sum of square of number {} and number {} is {}".format(x,y,n)



