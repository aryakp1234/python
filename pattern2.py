limit=int(input("Enter the row:"))
for i in range(limit+1,1,-1):
     for j in range(0,limit-1):
          print (" ", end="")
     for k in range(i,2*i-1):
            print ("*", end="")
     for k in range(2,i-1):
            print ("*", end="")
     print()

         
          



for i in range(1,limit+1):
    for j in range (limit-i):
        print (" ", end=" ")
    for j in range (2*i-1):
          print ("*", end=" ")
    print()
