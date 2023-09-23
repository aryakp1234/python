a=int(input("enter a number:"))
b=0
if a>1:
    for i in range (2,a):
        if (a%i)==0:
            b=1
            break
    if b :
        print ("number is  not prime")
    else:
         print ("number is prime")

       