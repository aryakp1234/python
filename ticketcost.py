a=int(input("Enter your age : "))
b=str(input("Enter The Day Of Weekend : "))
a1="wednesday"

if a<12 or a>65:
    ticketcost=5
    print("your ticket cost is=",ticketcost)
elif a>12 or a<18 and b==a1 :
    ticketcost=4
    print("your ticket cost is=",ticketcost)
else :
   ticketcost=8   
   print("your ticket cost is=",ticketcost)