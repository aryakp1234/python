# a=[1,2,3,4,5,6,4,3,2,7,10,21,1,34,10,15,16]
a=input("enter a list:")
b=[]
duplicatelist=[]
for i in a:
    if i not in b:
        b.append(i)
    elif i not in duplicatelist:
        duplicatelist.append(i)
        
print("duplicate values are:",duplicatelist)
print(b)