limit=int(input("Enter the raw:"))
for i in range(1,limit+1):
     for j in range(1,i+1):
          if j%2==1:
               print("5",end='')
          else:
               print("3",end='')
     print()

    
