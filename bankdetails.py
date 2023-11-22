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
       
         
    elif choice=="3":
            username=input("enter the username:")
            amount = int(input("Enter the deposit amount: "))
            for user_details in user_list:
                 if user_details["name"]==username:
                      user_details["bankbalance"]+=amount
                      print("Deposit successfull...!New bank balance:",user_details["bankbalance"])
              
    elif choice=="4":
            username=input("enter the username:")
            amount = int(input("Enter the amount to withdraw: ")) 
            for user_details in user_list:
                if user_details["name"]==username:
                    if user_details["bankbalance"]<=amount:
                         print("insufficiant")
                    else:
                        user_details["bankbalance"]-=amount
                        print("withdrawal successfull..!!New bank balance:",user_details["bankbalance"])
        
    elif choice=="5":
         print("program completed!!!")
         break
    else:
         print("invalid choice.please try again")
         
                 
