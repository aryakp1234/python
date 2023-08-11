price=int(input("Enter the total amount:"))
if  price>=100 :
    total=(price*10/100)
    print("discount :",total)
    print("Amount :",price-total)
else:
    print("No Discount ")    