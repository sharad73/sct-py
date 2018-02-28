#!/usr/bin
"""This programe will find the percentage margin of safty, percentage return
and P/BV*PE value of given stoc.
The output will be color coded as per below:
Margin of safty greater than 65% Green color
Margin of safty between 50% to 65% Orange color
Margin of safty less than 50% red color
One year return greater than 6% green color
One year return between 5% to 6% orange color
One year return less than 5% red color
"""
#Input Current market price
cmp = float(input("Please enter current market price :"))

#Input Book Value 
bv = float(input("Please enter book value :"))

#Input Earning per share
eps = float(input("Please enter EPS value :"))

#Function to calculate percentage
def percen(a):
    return float(100/(a))

#Function to calculate ratio of two values
def ratio(a,b):
    return a/b

#Function to calculate multiplication of two values
def value(a,b):
    return a*b

pe = ratio(cmp,eps) #Calculate current market price to earning per share ratio
pbv = ratio(cmp,bv) #Calculate current market price to book value per share ratio
mos = percen(pbv)   #Calculate margin of safty percentage
ret = percen(pe)    #Calculate annual return percentage
qul = value(pe,pbv) #Calculate valuation of share. If qul is less then 22.5, it could be a value pick

print "The margin of safty is {:.2f}%, earning is {:.2f}% and stock value is {:.2f}".format(mos,ret,qul)

