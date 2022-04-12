print("Please select the operation:\n (a) Add \n (b) Subtract \n (c) Multiply \n (d) Divide \n")
print("Select operation from a,b,c,d:")
selection=input()
print("Please enter the first number")
a=int(input())
print("PLease enter the second number")
b=int(input())

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

if (selection=='a'):
    print(a,"+",b ,"=", add(a,b))
    #x=add(a,b)
    #print(x)
elif (selection=='b'):    
    print(a,"-",b ,"=",sub(a,b))
    #x=sub(a,b)
    #print(x)
elif (selection=='c'):
    print(a,"*",b, "=",mult(a,b))
    #x=mult(a,b)
    #print(x)
elif (selection=='d'):
    print(a,"/",b ,"=",div(a,b))
    #x=div(a,b)
    #print(x)
