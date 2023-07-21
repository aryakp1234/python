print("enter the age the ticket price")

age = int(input("enter age :"))
day =input("enter the day")
if age < 12 or age >65 :
 price = 5
 print("the  ticket cost is 5")
 
elif age >12 and age <18 and  day== "wedensday":
  print("the ticket 4")
else:
    print("ticket is 8")
    
    

    

