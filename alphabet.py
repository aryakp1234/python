char = input('enter your character : ')
if((char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')):
  print(char, "is an Alphabet")
elif(char >= '0' and char <= '9'): 
  print(char, "is a Digit")
else :
   print("The Given Character ", char, "is a Special Character")