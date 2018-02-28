#!/usr/bin/python
i= 0
count = 0
sum = 0
list = []
while i < 6:
    n = (raw_input())
    list.append(int(n))
    count = count + 1
    sum = sum + list[i]
    i += 1
avg = sum/count
print avg


