list=[8,5,12,6,7]
print ("the length of list:",len(list))
print ("largest element is:",max(list))
max=list[0]
for i in range  (1,len(list)):
    if (list[i]>max):
        max=list[i]
        i=2
        if list[0]>list[4]:
            print("the value is",list[0])
        else:
            print ("the value is:",list[4])


print ("maximum index position:",list.index(max))
