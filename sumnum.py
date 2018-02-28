'''
Find the sum of a pair of numbers in a set equal to 8

'''

num1 = [1,2,3,9]
num2 = [1,2,4,5,3,4,7]

'''
For set num2
'''
k = 0
i = 0
j = 1
while k < len(num2):
    #print "The value of k is %d" %k 
    while i < len(num2):
        #print "The value of i is %d"  %i
        while j < len(num2):
            #print "The value of j is %d" %j
            pair_sum = num2[i] + num2[j]
            if pair_sum == 8:
                x = num2[i]
                y = num2[j]
                
                print 'In the given list %s: The sum is 8 for pair value %d, %d' %(num2,x,y)
            j = j + 1
        i = i + 1
        j = i + 1
    k = k + 1
    

