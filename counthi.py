"""
str = "abc hi ho"
count = 0
for i in range(len(str)):
    print i
    print "str[i:i+2]: ", str[i:i+2]
    if str[i:i+2] == 'hi':
        count = count +1
print count


# Return true if dog and cat appers in equal number in the given string, else False
str = "catcatdogxxxdog"
count_dog = 0
count_cat = 0

for i in range(len(str)):
    if 'dog' in str[i:i+3]:
        count_dog = count_dog + 1
    if 'cat' in str[i:i+3]:
        count_cat = count_cat + 1
if count_dog == count_cat:
    print True
else:
    print False
    
# If one string end with other string or vica versa, print True, else False
a = 'z'
b = '12xz'
ls =min(len(a),len(b))
print "ls: ",ls
if a[-ls:] == b[-ls:]:
    print True
else:
    print False

"""
"""
str = 'abcxyz'
j = '.'
for i in range(len(str)-4):
    print "str[i:i+4]: ", str[i:i+4]
    substr = str[i:i+4]
    
    if j not in substr[0] and 'xyz' in substr:
        print True
    else:
        print False
        """
str = 'The'

for str in str:
    print (str+str),
    
  
