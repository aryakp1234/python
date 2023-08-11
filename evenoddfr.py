k=[]
n=int(input("Enter the number:"))
k.append(n)
a=int(input("Enter the number:"))
k.append(a)
b=int(input("Enter the number:"))
k.append(b)
c=int(input("Enter the number:"))
k.append(c)
for i in k:
   if i%2==0:
        print("it is even and the number is:",i)
   else:
        print("it is odd and the number is ",i)
