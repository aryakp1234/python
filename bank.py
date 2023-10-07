user_list=[]
num_users=input("enter the number of users:")

print("USER INFORMATION:")
for user_details in user_list:
   
    user_details={
        "UserName:"
        "Branch:"
    }
    user_details['name']=input("enter your name:")
    user_details['address']=input("enter your address:")
    user_details['age']=input("enter your age:")
    user_details['contact_number']=input("enter your contact number:")
    user_list.append(user_details)

print(user_list)


