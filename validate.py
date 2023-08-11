pwd=str(input("Enter your password:"))

has_uppercase =False  
has_lowercase =False
has_digit =False
has_length=False

for char in pwd:
    if char.isupper():
     has_uppercase=True
    elif char.islower():
     has_lowercase=True
    elif char.isdigit():
     has_digit=True
    elif len(pwd)<8:
        print("password should be atleast 8 characters!")        

if has_uppercase==True and  has_lowercase==True and has_digit==True:
  print("validated")
else:
  print("something went wrong")  

