user_list=[]
num_users=int(input("enter the number of users:"))
for i in range(num_users):
    user_details={}
    user_details['name']=input("enter your name:")
    user_details['address']=input("enter your address:")
    user_details['age']=int(input("enter your age:"))
    user_details['contact_number']=input("enter your contact number:")
    user_list.append(user_details)
print("\nUSER INFORMATION:")
for user_details in user_list:
    print("name:",user_details["name"])
    print("address:",user_details["address"])
    print("age:",user_details["age"])
    print("contact_number:",user_details["contact_number"])
    print()