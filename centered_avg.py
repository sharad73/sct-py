"""
nums = [3,1,4,2,100]
nums.sort()
nums = nums[1:-1]
print nums
sum = 0
for i in nums:
    sum = sum + i
    print sum
print sum/len(nums)

nums = [1,2,13,2,1,13]

sum = 0
prev_was_13 = False
for number in nums:
    
    if prev_was_13:
      prev_was_13 = False
      continue
    
    if number == 13:
        prev_was_13 = True
    else:
        sum += number
      
print sum
"""
nums = [1,3,2,2]
for index, number in numerate(nums[:-1])
 

 
        
    
    
    


        
    
