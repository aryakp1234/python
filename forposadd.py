k=[]
n=int(input("Enter the number:"))
k.append(n)
a=int(input("Enter the number:"))
k.append(a)
b=int(input("Enter the number:"))
k.append(b)
c=int(input("Enter the number:"))
k.append(c)
print(k)

sum=0
for i in k:
    if i>=0:
         sum=sum+i
      
    elif i<=0:
        pass
    else:
        pass    
print("number is positive")            
print(sum)
    