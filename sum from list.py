"""l=[12,13,14,15,16,17]
sum=0
for i in l:
         sum=sum+i
         print(sum)        

l=[1,2,3,4,5,6,7,8]
odd=[]
even=[]
for i in l:
    if i%2==0:
        odd.append(i)
    else:  
        even.append(i)


print("actual numbers in list :",l)         
print("odd numbers are:",odd)         
print("even numbers are:",even)         

a=str(input("Enter a string:"))
b=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in a:
  if (i in b):
    count=count+1
    print(i ," is vowel")
    print (count)
  else:
    print(i,"is not vowel")
"""

l=[1,2,3,3,4,3,5,6,5,4]
a=[]
b=[]
print("list is:",l)
for i in l:
    if i not in a:
        a.append(i)
    elif i not in b:
        b.append(i)
print("duplicates are:",b)


