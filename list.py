a = ["white","orange","blue","pink"]
print(a)
print(a[0])

a.append("grey")
a.insert(0,"red")
a[1] = "black" 
print(a)

a.remove("black")
print(a)



b=[15,18,26,87]
c=a+b
print(c)

d=a[1]+a[3]
print(d)

a.reverse()
print(a)

#b.clear

#del b
b.sort()
print(b)

# tuple

t = (1,2,5,4,"abc",5,5)

# multiple datatypes
# allow duplicates
# store multiple values
# ordered ,indexed
# not allow modification
print(t)


t=(12,13,24,"archu","megh",24)
print(t)

t1=(23,45,65)
t2=(2,4,7)
t3=t1+t2
print(t3)

#to manipulate tuple

l=list(t1)  #convert to list
l.append(48) #add a item to list
u=tuple(l) #reconvert list to tuple
print(u) 
print(len(t1)) 
print(len(a))