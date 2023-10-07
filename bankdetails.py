user_list=[]
user_details={}    

while True:
    print("\n1.create user \n2.View User Details \n3.Deposit \n4.Withdraw \n5.Quit")
    choice=input("enter a choice:")
    if choice=="1":
        name=input("enter your name:")
        address=input("enter your address:")
        age=int(input("enter your age:"))
        contact_number=input("enter your contact number:")
        bankbalance=0
        user_details['name']=name
        user_details['address']=address
        user_details['age']=age
        user_details['contact_number']=contact_number   
        user_details['bankbalance']=bankbalance
        user_list.append(user_details.copy())
        print(user_list)

    elif choice=="2":
        print("\nUSER INFORMATION:")
        for user_details in user_list:
            print("name:",user_details["name"])
            print("address:",user_details["address"])
            print("age:",user_details["age"])
            print("contact_number:",user_details["contact_number"])
            print("bankbalance:",user_details["bankbalance"])
            print (user_list)
         
    elif choice=="3":
        name=input("Enter your name:")
        deposit_amount=float(input("Enter the deposit amount:"))
        for user_details in user_list:
            if user_details["name"]==name:
               user_details["bankbalance"]+=deposit_amount
               print ("deposit successfull")
            
    # elif choice=="4":







    # elif choice==5:
    #     print ("exiting program.")
    # else:
    #     print("invalid choice.choose a valid option")




