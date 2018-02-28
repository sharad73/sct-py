#!/usr/bin/python

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []

for i in some_list:
    
    if some_list.count(i) > 1:
        
        if i not in duplicate:
            duplicate.append(i)
            

print duplicate


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = set([x for x in some_list if some_list.count(x) > 1])
count = set(some_list) # Remove duplicate value and just print value once
print duplicate
print count


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
count = []
for i in some_list:
     count.append(i) 
print count
