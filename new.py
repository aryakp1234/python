a=(input("enter a string:"))
b=[]
pos=[]
for i in a:
    b.append(i)
print(b)

for j in b:
     if j in 'aeiou':
          print(j, b.index(j))
          pos.append(b.index(j))
print(pos)

