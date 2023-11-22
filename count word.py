# a=str(input("Enter a string:"))
# count=len(a.split())
# print("Word Count:",count)



# a=str(input("Enter a string:"))
# longst=max(a.split(),key=len)
# print("Longest word:",longst)
# print("length of longest is:",len(longst))

a=str(input("Enter a string:"))
upper="Z","A","Q","W","S","x","C","D","E","R","F","V","B","G","T","Y","H","N","M","J","U","I","K","L","O","P"
caseuppr=[]
for i in a:
   i=a.split()
   if i.startswith(upper):
    caseuppr.append(i)
    print(i)

   # print(i)