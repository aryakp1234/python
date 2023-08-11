limit=int(input("Enter the raw:"))
for i in range(1,limit+1):
    for j in range(1,i+1):
          if i!=0 and j==i:
               print("1",end='')
          else:
               print("2",end='')
    print()

    
