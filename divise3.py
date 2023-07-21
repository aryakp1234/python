a=int(input("enter a number:" ))
if(a%2==0)&(a%3==0):
    print("number is even and divisble by 3")  
elif(a%2==1)&(a%3==1):
    print("number is not even  and  not divisble by 3")
elif(a%2==0)&(a%3==1):
    print("number is even and not divisble by 3")    
else :
    print("number is not even  divisble by 3")
