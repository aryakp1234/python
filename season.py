month=int(input("Enter month:"))
day=int(input("Day:"))
d={
    1:"janu",
    2:"feb",
    3:"mar",
    4:"apr",
    5:"may",
    6:"june",
    7:"july",
    8:"aug",
    9:"sep",
    10:"oct",
    11:"nov",
    12:"dec"
}
if month==3 and day>=20 or month==4 or month==5 or month==6 and day<=20 :
    print("Spring")
elif month==6 and day>=21 or month==7 or month==8 or month==9 and day<=21 :
    print("Summer")
elif month==9 and day>=22 or month==10 or month==11 or month==12 and day<=20 :
    print("Fall")
else :
    print("Winter")