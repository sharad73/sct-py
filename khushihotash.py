
"""
for i in range(1000):
    print "Number of class tests, 0 to 3: \n"
    ct = int(raw_input())
    print "Number of lab report, 0 to 3: \n"
    lr = int(raw_input())
    print "class tests preparation time: 1 to 5 hrs: \n"
    ctp = int(raw_input())
    print "lab report preparation time: 1 to 5 hrs: \n"
    lrp = int(raw_input())
    print "Attending class time: 3 to 8 hrs: \n"
    ac = int(raw_input())
    time_spent = ct*ctp + lr*lrp + ac
    if time_spent <= 11:
        print "Khushi"
    else:
        print "Hotash"

    break
"""    
def khho(ct=0,lr=0,ctp=1,lrp=1,ac=3):
    time_spent = ct*ctp + lr*lrp + ac
    if time_spent <= 11:
        print "Khushi"
    else:
        print "Hotash"

    return

khho()
    
        
