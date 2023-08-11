"""
#1.equal or not
#------------
a=int(input("Enter First Number : " ))
b=int(input("Enter Second Number :" ))
if a==b:
    print(a, "and" ,b,"are equal")
else :
    print(a, "and" ,b,"are not equal")   
     
#2.casting your vote
#-----------------------

a=int(input("Enter The Age : "))
if a==21:
 print(" congratulations!! you are eligible for casting your vote")
else:
  print(" sorry (^_^) you are not eligible for casting your vote")
#3.largest among three
#--------------------------

x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))
if x>y and x>z:
    print(x,"is the largest number") 
elif y>x and y>z:
     print(y,"is the largest number")
else :
     print(z,"is the largest number") 

#4.eligible for admission
#------------------------

mm=int(input("Enter The marks obtained in mathmatics : "))
che=int(input("Enter The marks obtained in chemistry : "))
phy=int(input("Enter The marks obtained in physics : "))
total=int(input("Enter The total marks obtained : "))
mp=int(input("Enter The total marks obtained in maths and physics: "))
if mm>=65:
    print("candidate is eligible for admission")
elif phy>=55:    
    print("candidate is eligible for admission ") 
elif che>=50:
     print("candidate is eligible for admission")
elif total>=190:   
     print("candidate is eligible for admission")
elif mp>=140:
     print("candidate is eligible for admission")
else :
          print("candidate is not eligible for admission")
#triangle
#--------

a=int(input("Enter The right side of triangle :"))
b=int(input("Enter The right side of triangle :"))
c=int(input("Enter The right side of triangle :"))
if a==b or a==c or b==c:
    print("the triangle is isosceles")
elif a==b==c:
    print("the triangle is  equilateral")
else:
    print("the triangle is scalene")  

#type of data
#------------
a=input("enter the data=")
print("type of data is=",type(a))

#grade and description
#--------------------
a=str(input("enter the data="))
a1="E"
a2="V"
a3="G"
a4="A"
a5="F"
if a==a1:
    print("Excellent")
elif a==a2:
    print("Very good")
elif a==a3:
     print("Good")
elif a==a4:
    print("Average")
elif a==a5:
    print("Fail")
else:
     print("invalid grade")


#day of week
#-----------

a=int(input("enter the data="))
a1=1
a2=2
a3=3
a4=4
a5=5
a6=6
a7=7
if a==a1:
    print("sunday")
elif a==a2:
    print("monday")
elif a==a3:
     print("tuesday")
elif a==a4:
    print("wednesday")
elif a==a5:
    print("thursday")
elif a==a6:
    print("friday")
elif a==a7:
    print("saturday")    
else:
     print("invalid grade")

#Triangle
#--------

a=int(input("Enter The right side of triangle :"))
b=int(input("Enter The left side of triangle :"))
c=int(input("Enter The bottom side of triangle :"))
if a==b and a==c and b==c:
    print("the triangle is  equilateral")
elif a==b or b==c or a==c  :
    print("the triangle is isosceles")
else :
    print("the triangle is scalene")
     
     
a=(input("Enter the data:"))
print("type of data=",type(a)) 
       
         """