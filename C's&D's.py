a='do not delete other VMs without permision of concerned faculty'
c=0
d=0
for i in a:
    print (i)
    if i==c:
        print ("number of c's in the string is",c)
        c=c+1
    if i==d:
        print ("number of d's in the string is",d)
        d=d+1 
if c==d:
    print ("balanced")
else:
    print ("unbalanced")

