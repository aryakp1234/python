
a=str(input("Enter a string:"))
countU=0
countL=0
i=0
while i<len(a):
    if a[i].isupper():
        countU=countU+1
    elif a[i].islower():
        countL=countL+1
   
    i+=1        
print("no.of uppercase characters",countU)
print("no.of lowercase characters",countL)
        
    