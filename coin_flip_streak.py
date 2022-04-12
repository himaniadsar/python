import random
numberofstreaks=0
for i in range(10000):
    list1=[]
    for j in range(100):
        
        list1.append(random.choice(['Head','Tail']))
    Head_Tail=0
    last_seen=None
    for k in list1:
        if (last_seen==k):
            Head_Tail=Head_Tail+1
        else:
            Head_Tail=1
            last_seen=k
        if (Head_Tail==6):
            numberofstreaks=numberofstreaks+1
            break
print('Chance of streak: %s%%' % (numberofstreaks / 100))

                
