#def front_back(str):
str = 'code'

if len(str) == 1:
    print str
elif len(str) == 2:
    print str[-1] + str[0]
else:
  print str[-1] + str[1:-1] + str[0]
 
