print("eligibility for candidate")
m=int(input("marks in maths "))
p=int(input("marks in physics "))
c=int(input("marks in chemistry"))
total=m+p+c
total2=m+c

if(m>=65 and p>=55 and c>=50):
  if(total>=190 and total2>=140):

    print("eligible for admission")
else :
  print("not eligible")   