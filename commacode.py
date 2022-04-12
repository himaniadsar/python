def commacode(b):
    if len(b)==0:
        print ('')

    elif len(b)==1:
        print(b[0])
    
    elif len(b)>1:
        print(b[0],end="")
        for i in range (1,len(b)-1):
            print(" ,"+b[i], end="")   
        print(" and",b[len (b)-1])
        
    #print(b[0] + " and " + b[1])
spam=['apple','bananas', 'orange', 'tofu', 'cat']

commacode(spam)

