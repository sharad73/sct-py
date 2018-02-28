"""
nums = [1,2,3]
l_array = nums[-2:]
print l_array
l_array.append(nums[0])
print l_array


def fix_teen(n):
    if n in [13,14,17,18,19]:
        print 0
    else:
        print n

fix_teen(13)

"""
def round10(num):
    result = 10
    if num % 10 >= 5:
      result += (num/10)*10
    else:
        result = (num/10)*10
    print result

round10(14)
    


    

