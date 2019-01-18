#!/usr/bin/python3
#Function to find the greatest divisor of two number

#Multiple function finds multiples of given number starting from one to max i.e given number    
def multiple(m):
    multiple = []
    for i in range(1,m+1):      #Added m+1 because the range excludes the max value in iteration
        if m % i == 0:          #Modulus function finds the multiple of given number 
            multiple.append(i)  #Append the multiple in to empty multiple[]
    return (multiple)

def gcd(a,b):
    ma = multiple(a)
    mb = multiple(b)
    cf = []
    for f in ma:
        if f in mb:
            cf.append(f)
    print ("The Greatest Common Divisor of %d, %d is %d" %(a,b,cf[-1]))              #(cf[-1] prints right most multiple in the given list of common divisors. i.e. greatest common divisor
    
gcd(10,20)
         
