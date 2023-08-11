#if

a=int(input("enter a number:"))
if a>=0:
    print("the number is positive")
else:
    print("the number is negative")

    #largest number
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
if x<y :
    print(y,"is the largest number")
else:
    print(x,"is the largest number") 
    
    
#odd or even
a=int(input("enter a number:"))
if a%2==0:
    print("The Number is Even")
else:
    print("The Number is Odd")

#elif(largest among 3)


x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))
if x>y and x>z:
    print(x,"is the largest number") 
elif y>x and y>z:
     print(y,"is the largest number")
else :
     print(z,"is the largest number") 