ls = [1, 2, 9, 4, 5]
i = 9
if i in ls[0:4]:
    print True
else:
    print False



nums = [1,1,2,3,1]
for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
        print True
    print False

a = 'xxcaazz'
b = 'xxbaaz'
count = 0
for i in range(len(a)-1):
    sma = a[i:i+1]
    for j in range(len(b)-1):
        smb = b[i:i+1]
if sma == smb:
count = count + 1
print count

      
