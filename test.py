'''
Take two digit integer say 19 and calculate the square of each digit.
Add the square numbers and continue, until there sum become 1

'''

n = str('19')
while  n != 1:    
    print n
    li = list(n)
    print li
    x = int(li[0])
    y = int(li[1])
    x = int(x**2)
    y = int(y**2)
    n = str(int(x+y))
    
    
 
    
    
        
        







    
     
 
