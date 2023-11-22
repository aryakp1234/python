
sumeven=0
sumodd=0
a=int(input("enter a number :"))
i=0
while i<=a:
    if i%2==0:
     sumeven+=i
    else:
      sumodd+=i
    i+=1  
print("sum of odd number:",sumodd)      
print("sum of even number:",sumeven) 