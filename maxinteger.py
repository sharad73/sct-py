#!/usr/bin/python

'''
Find and print the max value in give list of integer'''
ls1 = [74,23,100,105,105,60] # Given list
length = len(ls1)
print("Number of items in the list:", length)
ls2 = []
for i in range(len(ls1)): #Outer loop to pop one value from the list and compare with remaining values in the list
    print("Outer loop iteration ##:", i)
    a2 = ls1.pop() # popped value stored in a2 variable
    print("Pooped value ######:", a2)
    
    
    for i in range(len(ls1)): #Inner loop to iterate through all the values in the list and compare with popped value
        print("Inner loop iteration #:", i)
        #print("a2:", a2)
        print("%d index has value %d in the list ls1: " %(i, ls1[i]))
        if a2 > ls1[i]:
            print("%d is grater than %d:" % (a2,ls1[i]))
            if len(ls2) == 0: 
                ls2.append(a2)
                print("Max value:", ls2)
            else:
                if ls2[0] < a2:
                    ls2[0] = a2
                    print("Max value:", ls2[0])    
        else:
            print("%d is less than %d:" % (a2,ls1[i]))
            if len(ls2) == 0: 
                ls2.append(ls1[i])
                print("Max value:", ls2)
            else:
                if ls2[0] < ls1[i]:
                    ls2[0] = ls1[i]
                    print("Max value:", ls2[0])

print("max_value in the given list is %d:" % (ls2[0]))
        
 

        

        
    
    
        
