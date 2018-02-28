lista = [1,5,6,9,3]
listb = [1,9,6,5]

missing = []
for i in lista:
    if i not in listb:
        missing.append(i)
        print missing
     
    
#CV This will print the 2nd duplicate item in the list
ls = ['This', 'is', 'a', 'file', 'file','file','data','having', 'data','The', 'data','file', 'has', 'large', 'data']
one_time = [] #Store non duplicate values
duplicate = []
while len(duplicate) < 2:
 
    for i in ls:
        if i not in one_time:
            one_time.append(i)
        else:
            if i not in duplicate:
                duplicate.append(i)
                
print duplicate[1]

# Another way of printing duplicate vaules, but not in any order
ls = ['This', 'is', 'a', 'file','data','having', 'data','The', 'file', 'has', 'large', 'data']
set_ls = set(ls)
#print "Set: %r" %(set_ls)
for item in set_ls:
    ls.remove(item)
print ls
