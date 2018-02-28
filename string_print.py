def front3(str):
  if len(str) < 3:
    return (str*3)
  else:
    front = []
    for i in str:
      if len(front) < 3:
        front.append(i)
    return "".join(front*3)
    


str = "a"
print str[:3]*3

